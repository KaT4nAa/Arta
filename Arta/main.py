import pygame
import sys
import json

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre de jeu
screen_width = 1200
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ARTA")

# Définir l'icône de la fenêtre
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Définir les couleurs
black = (0, 0, 0)
white = (255, 255, 255)

# Définir la police
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

# Charger les images des boutons
play_button_image = pygame.image.load("play_button.png")
play_button_hover_image = pygame.image.load("play_button_hover.png")
play_button_click_image = pygame.image.load("play_button_click.png")
quit_button_image = pygame.image.load("quit_button.png")
quit_button_hover_image = pygame.image.load("quit_button_hover.png")
quit_button_click_image = pygame.image.load("quit_button_click.png")
settings_button_image = pygame.image.load("settings_button.png")
settings_button_hover_image = pygame.image.load("settings_button_hover.png")
settings_button_click_image = pygame.image.load("settings_button_click.png")
actus_button_image = pygame.image.load("actus_button.png")
actus_button_hover_image = pygame.image.load("actus_button_hover.png")
actus_button_click_image = pygame.image.load("actus_button_click.png")

# Redimensionner les images des boutons si nécessaire
button_width, button_height = 184, 61
play_button_image = pygame.transform.scale(play_button_image, (button_width, button_height))
play_button_hover_image = pygame.transform.scale(play_button_hover_image, (button_width, button_height))
play_button_click_image = pygame.transform.scale(play_button_click_image, (button_width, button_height))
quit_button_image = pygame.transform.scale(quit_button_image, (button_width, button_height))
quit_button_hover_image = pygame.transform.scale(quit_button_hover_image, (button_width, button_height))
quit_button_click_image = pygame.transform.scale(quit_button_click_image, (button_width, button_height))
settings_button_image = pygame.transform.scale(settings_button_image, (button_width, button_height))
settings_button_hover_image = pygame.transform.scale(settings_button_hover_image, (button_width, button_height))
settings_button_click_image = pygame.transform.scale(settings_button_click_image, (button_width, button_height))
actus_button_image = pygame.transform.scale(actus_button_image, (button_width, button_height))
actus_button_hover_image = pygame.transform.scale(actus_button_hover_image, (button_width, button_height))
actus_button_click_image = pygame.transform.scale(actus_button_click_image, (button_width, button_height))

# Charger l'image du fond et la redimensionner à la taille de l'écran
background_image = pygame.image.load("background.jpg")  # Assurez-vous que le chemin soit correct
background_image = pygame.transform.scale(background_image, (1200, 500))

# Charger l'image de fond pour les actualités
actus_background_image = pygame.image.load("actus_background.jpg")
actus_background_image = pygame.transform.scale(actus_background_image, (screen_width, screen_height))

# Redimensionner les images des boutons retour
back_button_width, back_button_height = 184, 61
back_button_image = pygame.image.load("back_button.png")
back_button_hover_image = pygame.image.load("back_button_hover.png")
back_button_click_image = pygame.image.load("back_button_click.png")
back_button_image = pygame.transform.scale(back_button_image, (back_button_width, back_button_height))
back_button_hover_image = pygame.transform.scale(back_button_hover_image, (back_button_width, back_button_height))
back_button_click_image = pygame.transform.scale(back_button_click_image, (back_button_width, back_button_height))

# Créer les rectangles des boutons avec des coordonnées spécifiques
play_button_rect = pygame.Rect(790, 200, button_width, button_height)
settings_button_rect = pygame.Rect(790, 280, button_width, button_height)
quit_button_rect = pygame.Rect(790, 360, button_width, button_height)
actus_button_rect = pygame.Rect(75, 380, button_width, button_height)
back_button_rect = pygame.Rect(1000, 10, back_button_width, back_button_height)

# Fonction pour sauvegarder les clics dans un fichier
def save_clicks(clicks):
    with open("clicks.json", "w") as file:
        json.dump({"clicks": clicks}, file)

# Fonction pour charger les clics depuis un fichier
def load_clicks():
    try:
        with open("clicks.json", "r") as file:
            data = json.load(file)
            return data["clicks"]
    except FileNotFoundError:
        return 0

def main_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(mouse_pos):
                    game()  # Lancer le jeu si le bouton "Play" est cliqué
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                elif settings_button_rect.collidepoint(mouse_pos):
                    settings()  # Accéder aux paramètres
                elif actus_button_rect.collidepoint(mouse_pos):
                    actus_menu()  # Accéder au menu des actualités

        # Afficher le fond
        screen.blit(background_image, (0, 0))

        # Déterminer quelle image de bouton afficher pour le bouton "Play"
        if play_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                screen.blit(play_button_click_image, play_button_rect.topleft)
            else:
                screen.blit(play_button_hover_image, play_button_rect.topleft)
        else:
            screen.blit(play_button_image, play_button_rect.topleft)

        # Déterminer quelle image de bouton afficher pour le bouton "Quit"
        if quit_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                screen.blit(quit_button_click_image, quit_button_rect.topleft)
            else:
                screen.blit(quit_button_hover_image, quit_button_rect.topleft)
        else:
            screen.blit(quit_button_image, quit_button_rect.topleft)

        # Déterminer quelle image de bouton afficher pour le bouton "Settings"
        if settings_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                screen.blit(settings_button_click_image, settings_button_rect.topleft)
            else:
                screen.blit(settings_button_hover_image, settings_button_rect.topleft)
        else:
            screen.blit(settings_button_image, settings_button_rect.topleft)

            # Déterminer quelle image de bouton afficher pour le bouton "Actus"
            if actus_button_rect.collidepoint(mouse_pos):
                if mouse_click[0]:
                    screen.blit(actus_button_click_image, actus_button_rect.topleft)
                else:
                    screen.blit(actus_button_hover_image, actus_button_rect.topleft)
            else:
                screen.blit(actus_button_image, actus_button_rect.topleft)

            pygame.display.flip()

def game():
    clicks = load_clicks()

    button_width = 200
    button_height = 200
    button_x = (screen_width - button_width) // 2
    button_y = (screen_height - button_height) // 2

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_clicks(clicks)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                    clicks += 1
                elif back_button_rect.collidepoint(mouse_pos):
                    save_clicks(clicks)
                    return  # Retourne au menu principal

        screen.fill(black)

        pygame.draw.rect(screen, white, (button_x, button_y, button_width, button_height))

        text = font.render(f"Clics: {clicks}", True, white)
        screen.blit(text, (10, 10))

        # Afficher le bouton "Retour au menu"
        if back_button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:
                screen.blit(back_button_click_image, back_button_rect.topleft)
            else:
                screen.blit(back_button_hover_image, back_button_rect.topleft)
        else:
            screen.blit(back_button_image, back_button_rect.topleft)

        pygame.display.flip()

def settings():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Retourne au menu principal

        screen.fill(black)

        settings_text = large_font.render("Paramètres", True, white)
        settings_rect = settings_text.get_rect(center=(screen_width // 2, screen_height // 4))
        screen.blit(settings_text, settings_rect)

        back_text = font.render("Appuyez sur Échap pour retourner", True, white)
        back_rect = back_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(back_text, back_rect)

        pygame.display.flip()

def actus_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_pos):
                        return  # Retourne au menu principal

            screen.blit(actus_background_image, (0, 0))

            # Afficher le bouton "Retour au menu"
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if back_button_rect.collidepoint(mouse_pos):
                if mouse_click[0]:
                    screen.blit(back_button_click_image, back_button_rect.topleft)
                else:
                    screen.blit(back_button_hover_image, back_button_rect.topleft)
            else:
                screen.blit(back_button_image, back_button_rect.topleft)

            pygame.display.flip()

# Lancer le menu principal
main_menu()