import pygame

COULEUR_FOND = (255, 255, 255)
LARGEUR = 640
HAUTEUR = 480

pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Pokemon")

fenetre.fill(COULEUR_FOND)

logo = pygame.image.load("logo_pokemon.png").convert()
print("Dimension du logo", logo.get_size())

petit_logo = pygame.transform.scale(logo, (logo.get_width() // 1, logo.get_height() // 1))
petit_logo = petit_logo.convert()

fenetre.blit(petit_logo, (165, 5))

image_sacha = pygame.image.load("sacha_pikachu.png").convert()
print("Dimension du logo", image_sacha.get_size())

petite_image_sacha = pygame.transform.scale(image_sacha, (image_sacha.get_width() // 3, image_sacha.get_height() // 3))
petite_image_sacha = petite_image_sacha.convert()
fenetre.blit(petite_image_sacha, (225, 350))


# Paramètres du bouton "Jouer"
bouton_couleur = (252, 210, 28)  # Jaune
contour_couleur = (1, 49, 180)  # Gris pour le contour
taille_bouton = (200, 50)
position_bouton = (LARGEUR // 2 - taille_bouton[0] // 2, HAUTEUR // 2 - taille_bouton[1] // 2)

# Création d'un rectangle pour représenter le bouton
bouton_rect = pygame.Rect(position_bouton[0], position_bouton[1], taille_bouton[0], taille_bouton[1])

# Définition du contour du bouton
pygame.draw.rect(fenetre, contour_couleur, bouton_rect, 3)  # Dessiner le contour du bouton

# Dessiner le bouton avec sa couleur de remplissage (jaune)
pygame.draw.rect(fenetre, bouton_couleur, (bouton_rect.left + 3, bouton_rect.top + 3, taille_bouton[0] - 6, taille_bouton[1] - 6))

# Définition du texte "Jouer" avec la couleur bleu foncé
font = pygame.font.Font('pokemon.ttf', 36)
texte = font.render("Jouer", True, (1, 49, 180))  # Bleu foncé
texte_rect = texte.get_rect(center=bouton_rect.center)
fenetre.blit(texte, texte_rect)

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si le clic de souris est dans la zone du bouton
            if bouton_rect.collidepoint(event.pos):
                print("Le bouton Jouer a été cliqué!")
            
    pygame.display.flip()

pygame.quit()