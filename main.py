from pokemon import Pokemon

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
            print(self.nom_pokemons())
            while self.attaquant.get_en_vie() and self.defenseur.get_en_vie():
                self.attaquant.attaquer(self.defenseur)
                if self.defenseur.get_en_vie():
                    self.defenseur.attaquer(self.attaquant)

                # Échange des rôles entre attaquant et défenseur
                self.attaquant, self.defenseur = self.defenseur, self.attaquant

            print(self.nom_du_vainqueur())

pokemon_attaquant = Pokemon(1, "Bulbizarre", 1, 45, 49, 49, "Plante", 0)
pokemon_defenseur = Pokemon(2, "Salamèche", 1, 39, 52, 43, "Feu", 0)

combat = Combat(attaquant=pokemon_attaquant, defenseur=pokemon_defenseur)
combat.combattre_jusqua_fin()


