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
        Pokedex.ajouter_au_pokedex(ennemi)
        self.combat = Combat(joueur, ennemi)
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

        self.message_capturer_surface = self.police.render("Cliquer ici pour capturer le Pokémon", True, self.blanc)
        self.position_message_capturer = (100, 350)  # Position du texte à ajuster selon votre mise en page

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
                    x, y = pygame.mouse.get_pos()
                    if self.position_message_capturer[0] <= x <= self.position_message_capturer[0] + self.message_capturer_surface.get_width() and \
                        self.position_message_capturer[1] <= y <= self.position_message_capturer[1] + self.message_capturer_surface.get_height():
                        # Capturer le Pokémon et afficher le résultat
                        resultat_capturer = self.combat.capturer_pokemon() 
                        self.position_message_capturer = (30, 150) 
                        self.message_capturer_surface = self.police.render(resultat_capturer, True, self.orange)
                        self.fenetre.blit(self.message_capturer_surface, self.position_message_capturer)  # Afficher le résultat de la capture
                        pygame.display.flip()
                        
                        self.combat.fin_tour()
                        self.position_message_capturer = (100, 350)
                    else:
                        self.combat.jouer_tour()

            self.fenetre.blit(self.fond, (0, 0))
            self.afficher_barres_vie()
            self.afficher_noms_pokemon()
            self.afficher_pvs()
            self.afficher_images_pokemons()
            self.fenetre.blit(self.message_capturer_surface, self.position_message_capturer)

            if self.message_degats_surface:
                self.fenetre.blit(self.message_degats_surface, (100, 370))
            if self.message_pv_surface:
                self.fenetre.blit(self.message_pv_surface, (10, 120))
            pygame.display.flip()
           
            

    def afficher_barres_vie(self):
        pourcentage_vie_joueur = self.combat.pokemon_joueur.pv / self.combat.pokemon_joueur.pv_max
        pourcentage_vie_ennemi = self.combat.pokemon_ennemi.pv / self.combat.pokemon_ennemi.pv_max

        self.afficher_barre_vie(self.barre_vie_rect_joueur, pourcentage_vie_joueur, self.combat.pokemon_joueur, (self.vert, self.jaune, self.orange, self.rouge))
        self.afficher_barre_vie(self.barre_vie_rect_ennemi, pourcentage_vie_ennemi, self.combat.pokemon_ennemi, (self.vert, self.jaune, self.orange, self.rouge))

    def afficher_barre_vie(self, rect, pourcentage, pokemon, couleurs):
        couleur_barre = self.blanc

        if pourcentage >= 0.75:
            couleur_barre = self.vert
           
        elif 0.3 <= pourcentage < 0.75:
            couleur_barre = self.jaune
            
        elif 0.15 <= pourcentage < 0.3:
            couleur_barre = self.orange
           
        else:
            couleur_barre = self.rouge      
        pygame.draw.rect(self.fenetre, self.blanc, rect)
        pygame.draw.rect(self.fenetre, couleur_barre, (rect.x, rect.y, pourcentage * rect.width, rect.height))

    def afficher_noms_pokemon(self):
        nom_pokemon_joueur = self.police.render(self.combat.pokemon_joueur.nom, True, self.blanc)
        self.fenetre.blit(nom_pokemon_joueur, (self.barre_vie_rect_joueur.x, self.barre_vie_rect_joueur.y - 30))

        nom_pokemon_ennemi = self.police.render(self.combat.pokemon_ennemi.nom, True, self.blanc)
        self.fenetre.blit(nom_pokemon_ennemi, (self.barre_vie_rect_ennemi.x, self.barre_vie_rect_ennemi.y - 30))

    def afficher_pvs(self):
        pv_pokemon_joueur = self.police.render(f"{self.combat.pokemon_joueur.pv}/{self.combat.pokemon_joueur.pv_max}", True, self.blanc)
        self.fenetre.blit(pv_pokemon_joueur, (self.barre_vie_rect_joueur.x + self.barre_vie_rect_joueur.width + 10, self.barre_vie_rect_joueur.y))

        pv_pokemon_ennemi = self.police.render(f"{self.combat.pokemon_ennemi.pv}/{self.combat.pokemon_ennemi.pv_max}", True, self.blanc)
        self.fenetre.blit(pv_pokemon_ennemi, (self.barre_vie_rect_ennemi.x + self.barre_vie_rect_ennemi.width + 10, self.barre_vie_rect_ennemi.y))

    def charger_images_pokemons(self):
        images_pokemons = {}
        for pokemon in liste_151_pokemons:
            image_nom_fichier = f"images_pokemon/{pokemon.nom.lower()}.png"
            images_pokemons[pokemon.nom] = pygame.image.load(image_nom_fichier).convert_alpha()
        return images_pokemons
    
    def afficher_images_pokemons(self):
        image_joueur = self.images_pokemons[self.combat.pokemon_joueur.nom]
        image_ennemi = self.images_pokemons[self.combat.pokemon_ennemi.nom]

        # Position des images à ajuster en fonction de votre mise en page
        position_image_joueur = (100, 150)
        position_image_ennemi = (500, 10)

        self.fenetre.blit(image_joueur, position_image_joueur)
        self.fenetre.blit(image_ennemi, position_image_ennemi)


# Chargez les données depuis le fichier JSON
with open('pokemons.json', 'r') as file:
    data = json.load(file)

# Utilise les données pour créer la liste de Pokémon
liste_151_pokemons = [
    Pokemon(p["num"], p["nom"], p["niv"], p["pv"], p["att"], p["défense"], p["type"], p["évol"])
    for p in data
]

if __name__ == "__main__":
    pokemon_joueur = liste_151_pokemons
    pokemon_ennemi=random.choice(liste_151_pokemons)

    combat_graphique = CombatGraphique(pokemon_joueur, pokemon_ennemi)
    combat_graphique.afficher_interface()


