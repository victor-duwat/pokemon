import random
import json
import pygame
from pokedex import Pokedex
from pokemon import Pokemon

class Combat:
    def __init__(self, joueur, ennemi):
        self.pokemon_joueur = joueur
        self.pokemon_ennemi = ennemi
        self.pokedex = []
        self.tour = 0

    def nom_du_vainqueur(self):
        if self.pokemon_joueur.get_en_vie():
            return f"{self.pokemon_joueur.nom} est le vainqueur !"
        else:
            return f"{self.pokemon_ennemi.nom} est le vainqueur !"

    def nom_pokemons(self):
        return f"Le Pokémon joueur est {self.pokemon_joueur.nom} de type {self.pokemon_joueur.type}, et le Pokémon défenseur est {self.pokemon_ennemi.nom} de type {self.pokemon_ennemi.type}."

    def calculer_degats(self, attaquant, defenseur):
        type_attaquant = attaquant.type
        type_defenseur = defenseur.type

        multiplicateur_type = {
            'Eau': {'Feu': 2, 'Plante': 0.5, 'Sol': 2, 'Eau': 0.5},
            'Feu': {'Eau': 0.5, 'Plante': 2, 'Insecte': 2, 'Dragon': 0.5, 'Feu': 0.5},
            'Plante': {'Eau': 2, 'Feu': 0.5, 'Sol': 2, 'Dragon': 0.5, 'Insecte': 0.5, 'Plante': 0.5, 'Poison': 0.5, 'Vol': 0.5},
            'Sol': {'Feu': 2, 'Electrique': 2, 'Poison': 2,  'Plante': 0.5, 'Vol': 0.5, 'Insecte': 0.5},
            'Insecte': {'Plante': 2, 'Psy': 2, 'Feu': 0.5, 'Poison': 0.5, 'Fée': 0.5, 'Vol': 0.5},
            'Electrique': {'Eau': 2, 'Sol': 0.5, 'Vol': 2,  'Plante': 0.5, 'Electrique': 0.5, 'Poison': 0.5},
            'Vol': {'Combat': 2, 'Insecte': 2, 'Plante': 2, 'Electrique': 0.5},
            'Psy': {'Combat': 2, 'Poison': 2, 'Psy': 0.5},
            'Poison': {'Fée': 2, 'Plante': 2, 'Poison': 0.5, 'Sol': 0.5 },
            'Dragon': {'Dragon': 2, 'Fée': 0.5},
            'Fée': {'Dragon': 2, 'Combat': 2, 'Poison': 0.5, 'Feu': 0.5 },
            'Combat': {'Vol': 0.5, 'Psy': 0.5, 'Insecte': 0.5, 'Poison': 0.5}
        }
        if type_attaquant in multiplicateur_type and type_defenseur in multiplicateur_type[type_attaquant]:
            multiplier = multiplicateur_type[type_attaquant][type_defenseur]
            degats = int((2 * attaquant.niv / 5 + 2) * attaquant.att * multiplier / defenseur.défense)
            return max(degats, 1)  # Retourne soit les dégâts calculés, soit 1 si les dégâts sont égaux à zéro
        else:
            # Si les types ne sont pas pris en compte, retourner les dégâts en fonction de la défense du défenseur
            degats = int((2 * attaquant.niv / 5 + 2) * attaquant.att / defenseur.défense)
            return max(degats, 1)  # Retourne soit les dégâts calculés, soit 1 si les dégâts sont égaux à zéro

    def combattre_jusqua_fin(self):
        print(self.nom_pokemons())

    def jouer_tour(self):
        self.police = pygame.font.Font('pokemon.ttf', 17)
        self.blanc = (255, 255, 255)
        chance_echec = random.randint(1, 10)
        if self.tour == 0:
            if chance_echec == 1:
                self.message_degats_surface = self.police.render(f"{self.pokemon_joueur.nom} a raté son attaque.", True, self.blanc)
            else:
                degats_joueur = self.calculer_degats(self.pokemon_joueur, self.pokemon_ennemi)
                self.pokemon_ennemi.pv = max(0, self.pokemon_ennemi.pv - degats_joueur)
                self.message_degats_surface = self.police.render(f"{self.pokemon_joueur.nom} inflige {degats_joueur} points de dégâts à {self.pokemon_ennemi.nom}.", True, self.blanc)
                self.message_pv_surface = self.police.render(f"{self.pokemon_ennemi.nom} a maintenant {self.pokemon_ennemi.pv} points de vie.", True, self.blanc)

        elif self.tour == 1:
            if chance_echec == 1:
                self.message_degats_surface = self.police.render(f"{self.pokemon_ennemi.nom} a raté son attaque.", True, self.blanc)
            else:
                degats_ennemi = self.calculer_degats(self.pokemon_ennemi, self.pokemon_joueur)
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


    def fin_tour(self):
            from pnj import Jeu
            jeu_instance = Jeu(starter_choisi=self.pokemon_joueur)
            jeu_instance.run()

# Chargez les données depuis le fichier JSON
with open('pokemons.json', 'r') as file:
    data = json.load(file)

# Utilise les données pour créer la liste de Pokémon
liste_151_pokemons = [
    Pokemon(p["num"], p["nom"], p["niv"], p["pv"], p["att"], p["défense"], p["type"], p["évol"])
    for p in data
]