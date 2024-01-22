import pygame
from pnj import Jeu
from pokedex import Pokedex
from starter import SelectionStarter
import random
import sys
import pygame_gui

choix = SelectionStarter()


COULEUR_FOND = (255, 255, 255)
LARGEUR = 800
HAUTEUR = 600

pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Pokemon")

fond = pygame.image.load("bg_menu1.jpg")
fond = pygame.transform.scale(fond, (LARGEUR, HAUTEUR))

fenetre.blit(fond, (0, 0))

logo = pygame.image.load("logo_pokemon.png").convert_alpha()

petit_logo = pygame.transform.scale(logo, (logo.get_width() // 2, logo.get_height() // 2))
petit_logo = petit_logo.convert_alpha()
fenetre.blit(petit_logo, (213, 15))

image_sacha = pygame.image.load("sacha_pikachu.png").convert_alpha()

petite_image_sacha = pygame.transform.scale(image_sacha, (image_sacha.get_width() // 3, image_sacha.get_height() // 3))
petite_image_sacha = petite_image_sacha.convert_alpha()
fenetre.blit(petite_image_sacha, (300, 450))

bouton_couleur = (252, 210, 28)
contour_couleur = (1, 49, 180)
taille_bouton = (200, 90)
position_bouton = (LARGEUR // 2 - taille_bouton[0] // 2, HAUTEUR // 2 - taille_bouton[1] // 2)

bouton_rect = pygame.Rect(position_bouton[0], position_bouton[1], taille_bouton[0], taille_bouton[1])

pygame.draw.rect(fenetre, contour_couleur, bouton_rect, 3)

pygame.draw.rect(fenetre, bouton_couleur, (bouton_rect.left + 3, bouton_rect.top + 3, taille_bouton[0] - 6, taille_bouton[1] - 6))

font = pygame.font.Font('pokemon.ttf', 36)
texte = font.render("Jouer", True, (1, 49, 180))
texte_rect = texte.get_rect(center=bouton_rect.center)
fenetre.blit(texte, texte_rect)


continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_rect.collidepoint(event.pos):
                starter_choisi = choix.executer()
                jeu = Jeu(starter_choisi)
                jeu.starter_choisi = starter_choisi
                jeu.run()

    pygame.display.flip()

pygame.quit()
