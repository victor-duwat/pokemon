import pygame
import sys
import random
import json
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from combat import Combat
from pokemon import Pokemon
from pokedex import Pokedex


class CombatGraphique:
    def __init__(self, joueur, ennemi):
        self.combat = Combat(joueur, ennemi)
        self.pokemon_joueur = joueur
        self.pokemon_ennemi = ennemi
        self.message_degats_surface = None
        self.message_pv_surface = None

        # Initialisation de Pygame
        pygame.init()

        # Définir la taille de la fenêtre
        self.largeur, self.hauteur = 800, 400
        self.taille_fenetre = (self.largeur, self.hauteur)

        # Créer la fenêtre
        self.fenetre = pygame.display.set_mode(self.taille_fenetre)
        pygame.display.set_caption("Combat Pokémon")

        # Charger l'image du fond
        self.fond = pygame.image.load("fondcombat.png").convert()

        # Définir la position et la taille de la barre de vie
        self.barre_vie_rect_ennemi = pygame.Rect(100, 60, 200, 20)
        self.barre_vie_rect_joueur = pygame.Rect(500, 290, 200, 20)

        # Couleurs
        self.blanc = (255, 255, 255)
        self.vert = (50, 205, 50)
        self.jaune = (255, 215, 0)
        self.orange = (255, 140, 0)
        self.rouge = (255, 0, 0)

        # Police de caractères
        self.police = pygame.font.Font('pokemon.ttf', 17)

        self.tour = 0

    def afficher_interface(self):
        pygame.display.set_caption("Combat Pokémon")
        
        # Charger l'image du fond
        self.fond = pygame.image.load("fondcombat.png").convert()

        # Initialiser les images des Pokémon après la création de la fenêtre
        self.images_pokemons = self.charger_images_pokemons()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    self.jouer_tour()

            self.fenetre.blit(self.fond, (0, 0))
            self.afficher_barres_vie()
            self.afficher_noms_pokemon()
            self.afficher_pvs()
            self.afficher_images_pokemons()

            # Messages degats / vie
            if self.message_degats_surface:
                self.fenetre.blit(self.message_degats_surface, (100, 370))
            if self.message_pv_surface:
                self.fenetre.blit(self.message_pv_surface, (10, 120))
            pygame.display.flip()

    def fin_tour(self):
        from pnj import Jeu
        jeu_instance = Jeu(starter_choisi=self.pokemon_joueur)
        jeu_instance.run()

    def jouer_tour(self):
        chance_echec = random.randint(1, 10)
        if self.tour == 0:
            if chance_echec == 1:
                self.message_degats_surface = self.police.render(f"{self.pokemon_joueur.nom} a raté son attaque.", True, self.blanc)
            else:
                degats_joueur = self.combat.calculer_degats(self.pokemon_joueur, self.pokemon_ennemi)
                self.pokemon_ennemi.pv = max(0, self.pokemon_ennemi.pv - degats_joueur)
                self.message_degats_surface = self.police.render(f"{self.pokemon_joueur.nom} inflige {degats_joueur} points de dégâts à {self.pokemon_ennemi.nom}.", True, self.blanc)
                self.message_pv_surface = self.police.render(f"{self.pokemon_ennemi.nom} a maintenant {self.pokemon_ennemi.pv} points de vie.", True, self.blanc)

        elif self.tour == 1:
            if chance_echec == 1:
                self.message_degats_surface = self.police.render(f"{self.pokemon_ennemi.nom} a raté son attaque.", True, self.blanc)
            else:
                degats_ennemi = self.combat.calculer_degats(self.pokemon_ennemi, self.pokemon_joueur)
                self.pokemon_joueur.pv = max(0, self.pokemon_joueur.pv - degats_ennemi)
                self.message_degats_surface = self.police.render(f"{self.pokemon_ennemi.nom} inflige {degats_ennemi} points de dégâts à {self.pokemon_joueur.nom}.", True, self.blanc)
                self.message_pv_surface = self.police.render(f"{self.pokemon_joueur.nom} a maintenant {self.pokemon_joueur.pv} points de vie.", True, self.blanc)

        if not self.pokemon_joueur.get_en_vie():
            print(f"{self.pokemon_joueur.nom} est KO.")
            Pokedex.ajouter_au_pokedex(self.pokemon_ennemi)          
            self.fin_tour()

        elif not self.pokemon_ennemi.get_en_vie():
            print(f"{self.pokemon_ennemi.nom} est KO.")
            Pokedex.ajouter_au_pokedex(self.pokemon_ennemi)
            self.pokemon_joueur.niv += 1
            if self.pokemon_joueur.niv == 3:
                self.pokemon_joueur.évol += 1
                self.pokemon_joueur = liste_151_pokemons[self.pokemon_joueur.num]
            print(f"{self.pokemon_joueur.niv} niveau") 
            self.fin_tour()

        else:
            self.tour = 1 - self.tour  # Changer de tour entre 0 et 1

    def afficher_barres_vie(self):
        pourcentage_vie_joueur = self.pokemon_joueur.pv / self.pokemon_joueur.pv_max
        pourcentage_vie_ennemi = self.pokemon_ennemi.pv / self.pokemon_ennemi.pv_max

        self.afficher_barre_vie(self.barre_vie_rect_joueur, pourcentage_vie_joueur, self.pokemon_joueur, (self.vert, self.jaune, self.orange, self.rouge))
        self.afficher_barre_vie(self.barre_vie_rect_ennemi, pourcentage_vie_ennemi, self.pokemon_ennemi, (self.vert, self.jaune, self.orange, self.rouge))

    def afficher_barre_vie(self, rect, pourcentage, pokemon, couleurs):
        couleur_barre = self.blanc

        if pourcentage >= 0.75:
            couleur_barre = couleurs[0]
           
        elif 0.3 <= pourcentage < 0.75:
            couleur_barre = couleurs[1]
            
        elif 0.15 <= pourcentage < 0.3:
            couleur_barre = couleurs[2]
           
        else:
            couleur_barre = couleurs[3]      
        pygame.draw.rect(self.fenetre, self.blanc, rect)
        pygame.draw.rect(self.fenetre, couleur_barre, (rect.x, rect.y, pourcentage * rect.width, rect.height))

    def afficher_noms_pokemon(self):
        nom_pokemon_joueur = self.police.render(self.pokemon_joueur.nom, True, self.blanc)
        self.fenetre.blit(nom_pokemon_joueur, (self.barre_vie_rect_joueur.x, self.barre_vie_rect_joueur.y - 30))

        nom_pokemon_ennemi = self.police.render(self.pokemon_ennemi.nom, True, self.blanc)
        self.fenetre.blit(nom_pokemon_ennemi, (self.barre_vie_rect_ennemi.x, self.barre_vie_rect_ennemi.y - 30))

    def afficher_pvs(self):
        pv_pokemon_joueur = self.police.render(f"{self.pokemon_joueur.pv}/{self.pokemon_joueur.pv_max}", True, self.blanc)
        self.fenetre.blit(pv_pokemon_joueur, (self.barre_vie_rect_joueur.x + self.barre_vie_rect_joueur.width + 10, self.barre_vie_rect_joueur.y))

        pv_pokemon_ennemi = self.police.render(f"{self.pokemon_ennemi.pv}/{self.pokemon_ennemi.pv_max}", True, self.blanc)
        self.fenetre.blit(pv_pokemon_ennemi, (self.barre_vie_rect_ennemi.x + self.barre_vie_rect_ennemi.width + 10, self.barre_vie_rect_ennemi.y))

    def charger_images_pokemons(self):
        images_pokemons = {}
        for pokemon in liste_151_pokemons:
            image_nom_fichier = f"images_pokemon/{pokemon.nom.lower()}.png"
            images_pokemons[pokemon.nom] = pygame.image.load(image_nom_fichier).convert_alpha()
        return images_pokemons
    
    def afficher_images_pokemons(self):
        image_joueur = self.images_pokemons[self.pokemon_joueur.nom]
        image_ennemi = self.images_pokemons[self.pokemon_ennemi.nom]

        # Position des images à ajuster en fonction de votre mise en page
        position_image_joueur = (100, 150)
        position_image_ennemi = (500, 10)

        self.fenetre.blit(image_joueur, position_image_joueur)
        self.fenetre.blit(image_ennemi, position_image_ennemi)
            
# Chargez les données depuis le fichier JSON
with open('pokemons.json', 'r') as file:
    data = json.load(file)

# Utilisez les données pour créer la liste de Pokémon
liste_151_pokemons = [
    Pokemon(p["num"], p["nom"], p["niv"], p["pv"], p["att"], p["défense"], p["type"], p["évol"])
    for p in data
]


if __name__ == "__main__":

    pokemon_joueur = liste_151_pokemons
    
    pokemon_ennemi=random.choice(liste_151_pokemons)

    combat_graphique = CombatGraphique(pokemon_joueur, pokemon_ennemi)
    combat_graphique.afficher_interface()


