import pygame
import events
import classes
import statistic
import scores
import menu

WIDTH = 640  # ширина игрового окнав
HEIGHT = 480  # высота игрового окна
FPS = 30  # частота кадров в секунду


def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Паук против Мух")
    clock = pygame.time.Clock()
    clock.tick(FPS)
    player = classes.Player(screen)
    shots = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    events.create_enemies(screen, enemies)
    stats = statistic.Stats()
    score = scores.Score(screen, stats)

    while True:
        player.update()
        events.all_events(player, screen, shots, stats)
        events.update_screen(screen, player, shots, enemies, score)
        events.update_shots(shots, enemies, screen, stats, score)
        events.update_enemies(enemies, player, screen, shots, stats, score)


if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Паук против Мух")
    menu.show_menu(display, game)
