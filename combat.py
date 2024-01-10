class Combat:
    def __init__(self, joueur, ennemi):
        self.joueur = joueur
        self.ennemi = ennemi
        self.pokedex = []

    def nom_du_vainqueur(self):
        self.enregistrer_dans_pokedex(self.ennemi.type)
        if self.joueur.get_en_vie():
            return f"{self.joueur.nom} est le vainqueur !"
        else:
            return f"{self.ennemi.nom} est le vainqueur !"

    def nom_pokemons(self):
        return f"Le Pokémon joueur est {self.joueur.nom} de type {self.joueur.type}, et le Pokémon défenseur est {self.ennemi.nom} de type {self.ennemi.type}."

    def enregistrer_dans_pokedex(self, nom):
        if nom not in self.pokedex:
            self.pokedex.append(nom)
            print(f"{self.ennemi.nom} a été enregistré dans le Pokédex.")

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
            degats = int((2 * attaquant.niv / 5 + 2) * attaquant.att * multiplier / defenseur.defense)
            return degats
        else:
            return 0


    def combattre_jusqua_fin(self):
        print(self.nom_pokemons())

        print(self.nom_du_vainqueur())





