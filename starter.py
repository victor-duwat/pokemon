import pygame
import sys
from pokedex import Pokedex, Pokemon

class SelectionStarter:
    def __init__(self):
        pygame.init()

        self.largeur, self.hauteur = 600, 400
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Choix du Pokémon de départ")

        self.horloge = pygame.time.Clock()
        self.en_cours = True

        self.pokedex = Pokedex()
        self.boutons_starters = []

        self.image_carapuce = pygame.image.load("carapuce.png")
        self.image_carapuce = pygame.transform.scale(self.image_carapuce, (150, 150))

        self.image_salamèche = pygame.image.load("salameche.png")
        self.image_salamèche = pygame.transform.scale(self.image_salamèche, (150, 150))

        self.image_bulbizarre = pygame.image.load("bulbizarre.png")
        self.image_bulbizarre = pygame.transform.scale(self.image_bulbizarre, (150, 150))

        self.police = pygame.font.Font(None, 36)

        self.couleur_fond = (255, 255, 255)

        self.starter_selectionne = None

    def dessiner_boutons(self):
        hauteur_bouton = 150
        largeur_bouton = 150

        # Carapuce
        rect_carapuce = pygame.Rect(50, 125, largeur_bouton, hauteur_bouton)
        pygame.draw.rect(self.ecran, (0, 0, 255), rect_carapuce, 0)
        self.ecran.blit(self.image_carapuce, rect_carapuce)
        texte_carapuce = self.police.render("Carapuce", True, (0, 0, 0))
        self.ecran.blit(texte_carapuce, (rect_carapuce.centerx - texte_carapuce.get_width() // 2, 300))
        self.boutons_starters.append((rect_carapuce, self.pokedex.liste_starter[6]))  # Ajout du bouton

        # Salamèche
        rect_salamèche = pygame.Rect(250, 125, largeur_bouton, hauteur_bouton)
        pygame.draw.rect(self.ecran, (255, 0, 0), rect_salamèche, 0)
        self.ecran.blit(self.image_salamèche, rect_salamèche)
        texte_salamèche = self.police.render("Salamèche", True, (0, 0, 0))
        self.ecran.blit(texte_salamèche, (rect_salamèche.centerx - texte_salamèche.get_width() // 2, 300))
        self.boutons_starters.append((rect_salamèche, self.pokedex.liste_starter[3]))  # Ajout du bouton

        # Bulbizarre
        rect_bulbizarre = pygame.Rect(450, 125, largeur_bouton, hauteur_bouton)
        pygame.draw.rect(self.ecran, (0, 255, 0), rect_bulbizarre, 0)
        self.ecran.blit(self.image_bulbizarre, rect_bulbizarre)
        texte_bulbizarre = self.police.render("Bulbizarre", True, (0, 0, 0))
        self.ecran.blit(texte_bulbizarre, (rect_bulbizarre.centerx - texte_bulbizarre.get_width() // 2, 300))
        self.boutons_starters.append((rect_bulbizarre, self.pokedex.liste_starter[0]))  # Ajout du bouton

    def choisir_arriere_plan(self):
        chemin_arriere_plan = input("Entrez le chemin de l'image de fond : ")
        self.image_arriere_plan = pygame.image.load(chemin_arriere_plan)
        self.image_arriere_plan = pygame.transform.scale(self.image_arriere_plan, (self.largeur, self.hauteur))

    def gerer_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect_bouton, pokemon in self.boutons_starters:
                    if rect_bouton.collidepoint(pygame.mouse.get_pos()):
                        self.stocker_selection_starter(pokemon)
                        self.en_cours = False
                        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    self.choisir_arriere_plan()

    def stocker_selection_starter(self, pokemon):
        self.starter_selectionne = pokemon
        print(f"Vous avez choisi {pokemon.nom} !")
        print(self.starter_selectionne)
        return self.starter_selectionne

    def executer(self):
        while self.en_cours:
            self.gerer_evenements()

            self.ecran.fill(self.couleur_fond)

            texte_titre = self.police.render("Choisissez votre Pokémon", True, (0, 0, 0))
            self.ecran.blit(texte_titre, (self.largeur // 2 - texte_titre.get_width() // 2, 10))

            self.dessiner_boutons()

            pygame.display.flip()
            self.horloge.tick(30)

        starter = self.starter_selectionne
        return starter

if __name__ == "__main__":
    gui = SelectionStarter()
    gui.executer()
