import json
from pokemon import Pokemon


class Pokedex:
    # Chargez les données depuis le fichier JSON
    with open('pokemons.json', 'r') as file:
        data = json.load(file)

    # Utilisez les données pour créer la liste de Pokémon
    liste_starter = [
        Pokemon(p["num"], p["nom"], p["niv"], p["pv"], p["att"], p["défense"], p["type"], p["évol"])
        for p in data
        ]

    def __init__(self):
        self.pokemons = []
        self.équipe_pokemon = []

    @staticmethod
    def ajouter_au_pokedex(pokemon):
        with open('pokedex.json', 'r') as file:
            pokedex_data = json.load(file)

        # Vérifi si le Pokémon n'est pas déjà dans le Pokédex
        if pokemon.nom not in [p["nom"] for p in pokedex_data]:
            # Ajoutez le nouveau Pokémon au Pokédex
            nouveau_pokemon = {
                "nom": pokemon.nom,
                "num": pokemon.num,  
            }
            pokedex_data.append(nouveau_pokemon)

            # Enregistre les modifications dans le fichier
            with open('pokedex.json', 'w') as file:
                json.dump(pokedex_data, file, indent=2)

            print(f"{pokemon.nom} a été enregistré dans le Pokédex.")
            
        else:
            print(f"{pokemon.nom} est déjà dans le Pokédex.")

    def choisir_starter(self):
        print("Choisissez un Pokémon:")
        for i, starter in enumerate(self.liste_starter, start=1):
            print(f"{i}. {starter.nom}")

        choix_utilisateur = input("Entrez le numéro du Pokémon choisi: ")

        try:
            index_choisi = int(choix_utilisateur) - 1
            pokemon_choisi = self.liste_starter[index_choisi]
        except (ValueError, IndexError):
            print("Choix invalide. Veuillez choisir un numéro de 1 à 3.")
            return self.choisir_starter()

        print(f"Vous avez choisi {pokemon_choisi.nom}")
        self.équipe_pokemon.append(pokemon_choisi)
        return pokemon_choisi

pokedex = Pokedex()


