import pygame
import sys
import random
import pygame_gui
from pokedex import Pokemon
from combat import Combat
from pygame_combat import CombatGraphique
from starter import SelectionStarter
import json

class Jeu:
    def __init__(self, starter_choisi):
        pygame.init()

        self.largeur, self.hauteur = 800, 600
        self.blanc = (255, 255, 255)

        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Fenêtre Pygame")

        self.fond = pygame.image.load("fond.png")
        self.fond = pygame.transform.scale(self.fond, (self.largeur, self.hauteur))

        self.personnage_image = pygame.image.load("pnj1.png")
        self.personnage_image = pygame.transform.scale(self.personnage_image, (100, 100))

        self.joueur_image = pygame.image.load("joueur1.png")
        self.joueur_image = pygame.transform.scale(self.joueur_image, (50, 50))

        self.position_personnage = pygame.Rect(100, 300, 100, 100)
        self.position_joueur = pygame.Rect(400, 300, 100, 100)

        self.police = pygame.font.SysFont(None, 30)

        self.vitesse_joueur = 5
        self.clock = pygame.time.Clock()

        self.starter_choisi = starter_choisi

        # Initialisation de pygame_gui
        self.manager = pygame_gui.UIManager((self.largeur, self.hauteur))

        self.dialogue_window1 = pygame_gui.elements.UIWindow(
            pygame.Rect((200, 200), (400, 200)),
            self.manager,
            window_display_title="Dialogue",
            visible=False  # La fenêtre est invisible au démarrage
        )

        # Ajout du texte de dialogue pour la première fenêtre
        self.texte_dialogue1 = pygame_gui.elements.UITextBox(
            "",
            pygame.Rect((10, 10), (380, 180)),
            self.manager,
            container=self.dialogue_window1
        )

        # Création de la deuxième fenêtre de dialogue
        self.dialogue_window2 = pygame_gui.elements.UIWindow(
            pygame.Rect((200, 200), (400, 200)),
            self.manager,
            window_display_title="Dialogue",
            visible=False  # La fenêtre est invisible au démarrage
        )

        # Ajout du texte de dialogue pour la deuxième fenêtre
        self.texte_dialogue2 = pygame_gui.elements.UITextBox(
            "",
            pygame.Rect((10, 10), (380, 180)),
            self.manager,
            container=self.dialogue_window2
        )

        self.espace_relache = True 
        self.starter_choisi = None  
        self.zone_combat = pygame.Rect(80, 60, 250, 230)
        self.en_combat = False
        self.combat_lance = False
        self.probabilite_combat = 0.1
        self.deplacements = 0
        self.seuil_deplacements = random.randint(1,10)
        self.pokemon_joueur = starter_choisi

        # Chargez les données depuis le fichier JSON
        with open('pokemons.json', 'r') as file:
            data = json.load(file)

        # Utilisez les données pour créer la liste de Pokémon
        liste_151_pokemons = [
            Pokemon(p["num"], p["nom"], p["niv"], p["pv"], p["att"], p["défense"], p["type"], p["évol"])
            for p in data
        ]
        self.pokemon_ennemi=random.choice(liste_151_pokemons)

        # Création du bouton pour ouvrir le Pokédex
        self.btn_pokedex = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((580, 10), (100, 50)),
            text='Pokédex',
            manager=self.manager
        )
        
        # Définir la fonction à exécuter lorsque le bouton est cliqué
        self.btn_pokedex.when_clicked = self.ouvrir_pokedex

        # Création du bouton de retour
        self.btn_retour = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((690, 10), (100, 50)),
            text='Retour',
            manager=self.manager
        )
        self.btn_retour.when_clicked = self.retour_jeu

    def ouvrir_pokedex(self):
    # Charger les données depuis le fichier JSON "pokedex.json"
        with open('pokedex.json', 'r') as file:
            data = json.load(file)

        # Paramètres de la fenêtre
        largeur, hauteur = 800, 600
        blanc = (255, 255, 255)

        fenetre_pokedex = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Pokédex")

        police = pygame.font.SysFont(None, 30)

        # Boucle principale de la fenêtre du Pokédex
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.btn_retour:
                            running = False
                    

                # Gérer les événements de la bibliothèque pygame_gui
                self.manager.process_events(event)

            # Affichage des détails des Pokémon
            fenetre_pokedex.fill(blanc)
            y = 50
            for pokemon_data in data:
                nom = pokemon_data["nom"]
                num = pokemon_data["num"]
                texte = f"{num}: {nom}"
                texte_surface = police.render(texte, True, (0, 0, 0))
                fenetre_pokedex.blit(texte_surface, (50, y))
                y += 30

            # Mettre à jour et dessiner l'interface utilisateur du Pokédex
            self.manager.update(self.clock.tick(60) / 1000.0)
            self.manager.draw_ui(fenetre_pokedex)

            # Rafraîchir l'affichage de la fenêtre du Pokédex
            pygame.display.flip()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.manager.process_events(event)

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    self.espace_relache = True

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.btn_pokedex:
                            self.ouvrir_pokedex()
                
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.btn_retour:
                            self.retour_jeu()               

            self.gerer_input()

            # Vérifie la collision entre le joueur et le personnage
            collision = self.position_joueur.colliderect(self.position_personnage)

            if collision and not self.dialogue_window1.visible and self.espace_relache:
                self.dialogue_window1.show()
                self.texte_dialogue1.html_text = "Bienvenue dans le monde de Pokémon! Appuyez sur Espace pour voir de quoi votre équipe est composé."
                self.texte_dialogue1.rebuild()
                self.espace_relache = False

            if self.dialogue_window1.visible and self.espace_relache:
                self.dialogue_window1.hide()
                self.dialogue_window2.show()
                self.texte_dialogue2.html_text = 'Votre équipe :\n'

                if self.starter_choisi:
                    self.texte_dialogue2.html_text += f'{self.pokemon_joueur.nom}\n'
                else :
                    self.texte_dialogue2.html_text += f'{self.pokemon_joueur.nom}\n'

                self.texte_dialogue2.rebuild()
                self.espace_relache = False

            if self.dialogue_window2.visible and self.espace_relache:
                self.dialogue_window2.hide()
                self.espace_relache = False

            collision_zone_combat = self.position_joueur.colliderect(self.zone_combat)

            if collision_zone_combat and self.deplacements % self.seuil_deplacements == 0:
                if random.random() < self.probabilite_combat:
                    self.lancer_combat()

            self.ajuster_position_joueur()

            # Affiche le fond une seule fois
            self.fenetre.blit(self.fond, (0, 0))

            # Affiche le pnj et le joueur
            self.afficher_pnj()
            self.afficher_joueur()

            self.manager.update(self.clock.tick(60) / 1000.0)
            self.manager.draw_ui(self.fenetre)
            pygame.display.flip()

    def retour_jeu(self):
        pygame.quit()

    def gerer_input(self):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT]:
            self.position_joueur.x -= self.vitesse_joueur
            self.deplacements += 1
        elif touches[pygame.K_RIGHT]:
            self.position_joueur.x += self.vitesse_joueur
            self.deplacements += 1
        elif touches[pygame.K_UP]:
            self.position_joueur.y -= self.vitesse_joueur
            self.deplacements += 1
        elif touches[pygame.K_DOWN]:
            self.position_joueur.y += self.vitesse_joueur
            self.deplacements += 1

        # Vérifiez si la touche Espace est enfoncée
        if touches[pygame.K_SPACE] and self.espace_relache:
            self.espace_relache = False

        if self.est_dans_zone_combat():
            if not self.en_combat and self.deplacements == self.seuil_deplacements:
                self.lancer_combat()      

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
        if not self.est_dans_zone_combat():
            if self.en_combat:
                self.combat_lance = False

    def afficher_zone_combat(self):
        surface = pygame.Surface((self.zone_combat.width, self.zone_combat.height), pygame.SRCALPHA)
        pygame.draw.rect(surface, (0, 0, 0, 0), surface.get_rect(), 0)
        self.fenetre.blit(surface, (self.zone_combat.x, self.zone_combat.y))

    def lancer_combat(self):
        if not self.combat_lance and not self.en_combat:
            print("Combat lancé")
            self.en_combat = True
            self.combat_lance = True
            self.deplacements = 0 
            self.seuil_deplacements = 1
            self.combattant()
            combat_graphique = CombatGraphique(self.pokemon_joueur, self.pokemon_ennemi)
            combat_graphique.afficher_interface()

    def combattant(self):
            combat = Combat(joueur=self.pokemon_joueur, ennemi=self.pokemon_ennemi)
            combat.combattre_jusqua_fin()

    def est_dans_zone_combat(self):
        return self.zone_combat.colliderect(self.position_joueur)
    def afficher_pnj(self):
        self.fenetre.blit(self.personnage_image, self.position_personnage.topleft)

    def afficher_joueur(self):
        self.fenetre.blit(self.joueur_image, self.position_joueur.topleft)


if __name__ == "__main__":
    choix = SelectionStarter()
    starter_choisi = choix.executer()
    jeu = Jeu(starter_choisi)
    jeu.run()