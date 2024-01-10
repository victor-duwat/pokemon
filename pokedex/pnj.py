import pygame
import sys
import pygame_gui

class Jeu:
    def __init__(self):
        pygame.init()

        self.largeur, self.hauteur = 800, 600
        self.blanc = (255, 255, 255)

        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Fenêtre Pygame")

        self.fond = pygame.image.load("fond.png")
        self.fond = pygame.transform.scale(self.fond, (self.largeur, self.hauteur))

        self.personnage_image = pygame.image.load("pnj1.png")
        self.personnage_image = pygame.transform.scale(self.personnage_image, (100, 100))

        self.position_personnage = pygame.Rect(100, 300, 100, 100)
        self.position_joueur = pygame.Rect(400, 300, 20, 20)

        self.police = pygame.font.SysFont(None, 30)

        self.vitesse_joueur = 5
        self.clock = pygame.time.Clock()

        # Initialisation de pygame_gui
        self.manager = pygame_gui.UIManager((self.largeur, self.hauteur))

        # Création de la fenêtre de dialogue
        self.dialogue_window = pygame_gui.elements.UIWindow(
            pygame.Rect((200, 200), (400, 200)),
            self.manager,
            window_display_title="Dialogue",
            visible=False  # La fenêtre est invisible au démarrage
        )

        # Ajout du texte de dialogue
        self.texte_dialogue = pygame_gui.elements.UITextBox(
            "",
            pygame.Rect((10, 10), (380, 180)),
            self.manager,
            container=self.dialogue_window
        )

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.gerer_input()

            # Vérifiez la collision entre le joueur et le personnage
            collision = self.position_joueur.colliderect(self.position_personnage)

            if collision:
                self.dialogue_window.show()  # Affichez la fenêtre de dialogue
                self.texte_dialogue.html_text = "Bienvenue dans le monde de Pokémon! Appuyez sur Espace pour fermer."
                self.texte_dialogue.rebuild()

            self.ajuster_position_joueur()

            self.afficher()

            self.manager.update(self.clock.tick(60) / 1000.0)
            self.manager.draw_ui(self.fenetre)
            pygame.display.flip()

    def gerer_input(self):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT]:
            self.position_joueur.x -= self.vitesse_joueur
        if touches[pygame.K_RIGHT]:
            self.position_joueur.x += self.vitesse_joueur
        if touches[pygame.K_UP]:
            self.position_joueur.y -= self.vitesse_joueur
        if touches[pygame.K_DOWN]:
            self.position_joueur.y += self.vitesse_joueur

        # Fermez la fenêtre de dialogue avec la touche Espace
        if touches[pygame.K_SPACE] and self.dialogue_window.is_enabled():
            self.dialogue_window.hide()

    def ajuster_position_joueur(self):
        # Empêchez le joueur de traverser le personnage
        if self.position_joueur.colliderect(self.position_personnage):
            if self.position_joueur.x < self.position_personnage.x:
                self.position_joueur.x = self.position_personnage.x - self.position_joueur.width
            elif self.position_joueur.x > self.position_personnage.x:
                self.position_joueur.x = self.position_personnage.x + self.position_personnage.width
            if self.position_joueur.y < self.position_personnage.y:
                self.position_joueur.y = self.position_personnage.y - self.position_joueur.height
            elif self.position_joueur.y > self.position_personnage.y:
                self.position_joueur.y = self.position_personnage.y + self.position_personnage.height

    def afficher(self):
        self.fenetre.blit(self.fond, (0, 0))
        self.fenetre.blit(self.personnage_image, self.position_personnage.topleft)
        pygame.draw.rect(self.fenetre, (0, 0, 255), self.position_joueur)

if __name__ == "__main__":
    jeu = Jeu()
    jeu.run()
