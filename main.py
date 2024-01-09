class Pokemon:
    def __init__(self, num, nom, niv, pv, att, defense, type, evol):
        self.num = num
        self.nom = nom
        self.pv = pv
        self.niv = niv
        self.att = att
        self.defense = defense
        self.type = type
        self.evol = evol

    def get_en_vie(self):
        return self.pv > 0

    def attaquer(self, adversaire):
        degats = adversaire.subir_degats(self.att, self.type, adversaire.type)
        print(f"{self.nom} inflige {degats} points de dégâts à {adversaire.nom}.")

    def subir_degats(self, attaque_adversaire, type_attaquant, type_defenseur):
        multiplicateur_type = {
            'Eau': {'Feu': 2, 'Plante': 0.5, 'Terre': 0.5},
            'Feu': {'Eau': 0.5, 'Plante': 2, 'Terre': 0.5},
            'Plante': {'Eau': 2, 'Feu': 0.5, 'Terre': 2},
            'Terre': {'Eau': 2, 'Feu': 2, 'Plante': 0.5},
            'Insecte': {'Plante': 2, 'Feu': 0.5, 'Terre': 1},
            'Eclair': {'Eau': 2, 'Terre': 0.5, 'Vol': 2}
        }

        if type_attaquant in multiplicateur_type and type_defenseur in multiplicateur_type[type_attaquant]:
            multiplier = multiplicateur_type[type_attaquant][type_defenseur]
            degats = int((2 * self.niv / 5 + 2) * attaque_adversaire * multiplier / self.defense)
            self.pv = max(0, self.pv - degats)
            print(f"{self.nom} a maintenant {self.pv} points de vie.")
            return degats


class Combat:
    def __init__(self, attaquant, defenseur):
        self.attaquant = attaquant
        self.defenseur = defenseur
        self.pokedex = []

    def nom_du_vainqueur(self):
        if self.defenseur.get_en_vie():
            return "Aucun vainqueur, le combat n'est pas encore terminé."
        else:
            self.enregistrer_dans_pokedex(self.defenseur.type)
            return f"{self.attaquant.nom} est le vainqueur !"

    def nom_pokemons(self):
        return f"Le Pokémon attaquant est {self.attaquant.nom} de type {self.attaquant.type}, et le Pokémon défenseur est {self.defenseur.nom} de type {self.defenseur.type}."

    def enregistrer_dans_pokedex(self, nom):
        if nom not in self.pokedex:
            self.pokedex.append(nom)
            print(f"{self.defenseur.nom} a été enregistré dans le Pokédex.")

    def combattre_jusqua_fin(self):
        while self.attaquant.get_en_vie() and self.defenseur.get_en_vie():
            self.attaquant.attaquer(self.defenseur)
            if self.defenseur.get_en_vie():
                self.defenseur.attaquer(self.attaquant)

            # Échange des rôles entre attaquant et défenseur
            self.attaquant, self.defenseur = self.defenseur, self.attaquant

        print(self.nom_du_vainqueur())
        print(self.nom_pokemons())

# Exemple d'utilisation
pokemon_attaquant = Pokemon(1, "Bulbizarre", 1, 45, 49, 49, "Plante", 0)
pokemon_defenseur = Pokemon(2, "Salamèche", 1, 39, 52, 43, "Feu", 0)

combat = Combat(attaquant=pokemon_attaquant, defenseur=pokemon_defenseur)
combat.combattre_jusqua_fin()


