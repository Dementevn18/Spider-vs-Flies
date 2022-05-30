import pygame.font
from pygame.sprite import Group
from classes import Heart


class Score:
    """вывод игровой информации"""
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_colour = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.draw_image_score()
        self.draw_record()
        self.image_lifes()

    def draw_image_score(self):
        """Вырисовывает счет"""
        self.score_image = self.font.render(str(self.stats.score), True, self.text_colour, (0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def draw_record(self):
        """Вырисовывает рекорд"""
        self.record_image = self.font.render(str(self.stats.record), True, self.text_colour, (0, 0, 0))
        self.record_rect = self.record_image.get_rect()
        self.record_rect.centerx = self.screen_rect.centerx
        self.record_rect.top = self.screen_rect.top + 20

    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.record_image, self.record_rect)
        self.lifes.draw(self.screen)

    def image_lifes(self):
        """кол-во жизней"""
        self.lifes = Group()
        for life_number in range(self.stats.player_life):
            life = Heart(self.screen)
            life.rect.x = 15 + life_number * life.rect.width
            life.rect.y = 20
            self.lifes.add(life)
