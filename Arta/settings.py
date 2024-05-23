import pygame
import sys

def settings(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Retourne au menu principal

        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 72)
        settings_text = font.render("Paramètres", True, (255, 255, 255))
        settings_rect = settings_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4))
        screen.blit(settings_text, settings_rect)

        font = pygame.font.Font(None, 36)
        back_text = font.render("Appuyez sur Échap pour retourner", True, (255, 255, 255))
        back_rect = back_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(back_text, back_rect)

        pygame.display.flip()
