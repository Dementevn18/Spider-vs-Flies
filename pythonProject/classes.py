import pygame
import os


WIDTH = 640  # ширина игрового окна
HEIGHT = 480  # высота игрового окна
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'pictures')
spider_images = [pygame.image.load(os.path.join(img_folder, 'паук (1).png')),
                 pygame.image.load(os.path.join(img_folder, 'паук (2).png')),
                 pygame.image.load(os.path.join(img_folder, 'паук (3).png')),
                 pygame.image.load(os.path.join(img_folder, 'паук (4).png')),
                 pygame.image.load(os.path.join(img_folder, 'паук (5).png')),
                 pygame.image.load(os.path.join(img_folder, 'паук (6).png'))]
image_counter = 0


class Player(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.image = spider_images
        self.rect = self.image[1].get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right:
            self.center += 0.1
        if self.move_left:
            self.center -= 0.1
        if self.rect.left > WIDTH:
            self.center = 0
        if self.rect.right < 0:
            self.center = WIDTH

        self.rect.centerx = self.center

    def create_player(self):
        """создают игрока"""
        self.center = self.screen_rect.centerx

    def draw_player(self):
        global image_counter
        if image_counter == 600:
            image_counter = 0
        self.image[image_counter // 100].set_colorkey('WHITE')
        self.screen.blit(self.image[image_counter // 100], self.rect)
        image_counter += 1


class SpiderWeb(pygame.sprite.Sprite):

    def __init__(self, screen, player):
        super(SpiderWeb, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 6, 9)
        self.colour = 60, 60, 60
        self.speed = 0.25
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)


class Fly(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Fly, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join(img_folder, 'муха.png')).convert()
        self.image.set_colorkey('WHITE')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """отрисовка изображения"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.009
        self.rect.y = self.y


class Heart(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Heart, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join(img_folder, 'жизнь.png')).convert()
        self.image.set_colorkey('WHITE')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

