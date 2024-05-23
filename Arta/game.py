import pygame
import sys

def game(screen, background_image):
    clicks = 0
    button_width = 200
    button_height = 200
    button_x = (screen.get_width() - button_width) // 2
    button_y = (screen.get_height() - button_height) // 2

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                    clicks += 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return  # Retourne au menu principal

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255), (button_x, button_y, button_width, button_height))

        font = pygame.font.Font(None, 36)
        text = font.render(f"Clics: {clicks}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()