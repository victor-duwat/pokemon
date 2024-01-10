import pygame
import sys
import random
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from pokemon import Pokemon
from combat import Combat


pokemon_joueur = Pokemon(2, "Salamèche", 1, 29, 52, 43, "Feu", 0)
pokemon_ennemi = Pokemon(1, "Bulbizarre", 1, 45, 49, 49, "Plante", 0)

combat = Combat(joueur=pokemon_joueur, ennemi=pokemon_ennemi)
combat.combattre_jusqua_fin()

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 400
taille_fenetre = (largeur, hauteur)

# Créer la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Combat pokémon")

# Charger l'image du fond
fond = pygame.image.load("fondcombat.png").convert()

# Définir la position et la taille de la barre de vie
barre_vie_rect_1 = pygame.Rect(100, 60, 200, 20)
barre_vie_rect_2 = pygame.Rect(500, 290, 200, 20)

# Couleurs
blanc = (255, 255, 255)
vert = (50, 205, 50)
jaune = (255, 215, 0)
orange = (255, 140, 0)
rouge = (255, 0, 0)

# Police de caractères
police = pygame.font.Font('pokemon.ttf', 17)

# Calcul du pourcentage de vie restant
pourcentage_vie_joueur = pokemon_joueur.pv / pokemon_joueur.pv_max
pourcentage_vie_ennemi = pokemon_ennemi.pv / pokemon_ennemi.pv_max

tour = 0

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:  # Vérifie si un bouton de la souris est enfoncé
            chance_echec = random.randint(1, 10)

            # Tour du joueur
            if tour == 0:
                if chance_echec == 1:
                    print(f"{pokemon_joueur.nom} a raté son attaque.")
                else:
                    degats_joueur = combat.calculer_degats(pokemon_joueur, pokemon_ennemi)
                    pokemon_ennemi.pv = max(0, pokemon_ennemi.pv - degats_joueur)
                    print(f"{pokemon_joueur.nom} inflige {degats_joueur} points de dégâts à {pokemon_ennemi.nom}.")
                    print(f"{pokemon_ennemi.nom} a maintenant {pokemon_ennemi.pv} points de vie.")

            # Tour de l'ennemi
            elif tour == 1:
                if chance_echec == 1:  
                    print(f"{pokemon_ennemi.nom} a raté son attaque.")
                else:    
                    degats_ennemi = combat.calculer_degats(pokemon_ennemi, pokemon_joueur)
                    pokemon_joueur.pv = max(0, pokemon_joueur.pv - degats_ennemi)
                    print(f"{pokemon_ennemi.nom} inflige {degats_ennemi} points de dégâts à {pokemon_joueur.nom}.")
                    print(f"{pokemon_joueur.nom} a maintenant {pokemon_joueur.pv} points de vie.")

            # Vérifier si un Pokémon est KO avant de passer au tour suivant
            if not pokemon_joueur.get_en_vie():
                print(f"{pokemon_joueur.nom} est KO.")
                # Ajoutez ici toute autre logique pour le cas où le joueur est vaincu.
            elif not pokemon_ennemi.get_en_vie():
                print(f"{pokemon_ennemi.nom} est KO.")
                # Ajoutez ici toute autre logique pour le cas où l'ennemi est vaincu.
            else:
                tour = 1 - tour  # Changer de tour entre 0 et 1

    fenetre.blit(fond, (0, 0))

        # Barre de vies
    if pourcentage_vie_joueur >= 0.75:
        couleur_barre_2 = vert
        couleur_texte_joueur = vert
    elif 0.3 <= pourcentage_vie_joueur < 0.75:
        couleur_barre_2 = jaune
        couleur_texte_joueur = jaune
    elif 0.15 <= pourcentage_vie_joueur < 0.3:
        couleur_barre_2 = orange
        couleur_texte_joueur = orange
    else:
        couleur_barre_2 = rouge
        couleur_texte_joueur = rouge

    if pourcentage_vie_ennemi >= 0.75:
        couleur_barre_1 = vert
        couleur_texte_ennemi = vert
    elif 0.3 <= pourcentage_vie_ennemi < 0.75:
        couleur_barre_1 = jaune
        couleur_texte_ennemi = jaune
    elif 0.15 <= pourcentage_vie_ennemi < 0.3:
        couleur_barre_1 = orange
        couleur_texte_ennemi = orange
    else:
        couleur_barre_1 = rouge
        couleur_texte_ennemi = rouge


    # Calcul du pourcentage de vie restant
    pourcentage_vie_joueur = pokemon_joueur.pv / pokemon_joueur.pv_max
    pourcentage_vie_ennemi = pokemon_ennemi.pv / pokemon_ennemi.pv_max

    # Barre de vies
    pygame.draw.rect(fenetre, blanc, barre_vie_rect_2)
    pygame.draw.rect(fenetre, couleur_barre_2, (barre_vie_rect_2.x, barre_vie_rect_2.y, pourcentage_vie_joueur * barre_vie_rect_2.width, barre_vie_rect_2.height))

    pygame.draw.rect(fenetre, blanc, barre_vie_rect_1)
    pygame.draw.rect(fenetre, couleur_barre_1, (barre_vie_rect_1.x, barre_vie_rect_1.y, pourcentage_vie_ennemi * barre_vie_rect_1.width, barre_vie_rect_1.height))

    # Affichage des noms des Pokémon
    nom_pokemon_joueur = police.render(pokemon_joueur.nom, True, blanc)
    fenetre.blit(nom_pokemon_joueur, (barre_vie_rect_2.x, barre_vie_rect_2.y - 30))

    nom_pokemon_ennemi = police.render(pokemon_ennemi.nom, True, blanc)
    fenetre.blit(nom_pokemon_ennemi, (barre_vie_rect_1.x, barre_vie_rect_1.y - 30))

    # Affichage des PV sous forme "PV restants / PV total"
    pv_pokemon_joueur = police.render(f"{pokemon_joueur.pv}/{pokemon_joueur.pv_max}", True, couleur_texte_joueur)
    fenetre.blit(pv_pokemon_joueur, (barre_vie_rect_2.x + barre_vie_rect_2.width + 10, barre_vie_rect_2.y))

    pv_pokemon_ennemi = police.render(f"{pokemon_ennemi.pv}/{pokemon_ennemi.pv_max}", True, couleur_texte_ennemi)
    fenetre.blit(pv_pokemon_ennemi, (barre_vie_rect_1.x + barre_vie_rect_1.width + 10, barre_vie_rect_1.y))

    # Rafraîchir l'écran
    pygame.display.flip()