import pygame
import os
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'pictures')


def print_text(screen, message, x, y, font_colour=(0, 0, 0), font_type='font_from_games.otf', font_size=30):
    font_type = os.path.join(img_folder, font_type)
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    screen.blit(text, (x, y))


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (240, 230, 140)
        self.active_color = (253, 233, 16)

    def draw(self, screen, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x < mouse[0] < x + self.width) and (y < mouse[1] < y + self.height):
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))

            if (click[0] == 1) and (action is not None):
                if action == quit:
                    pygame.quit()
                    quit()
                action()

        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))

        print_text(screen=screen, message=message, x=x + 25, y=y + 10, font_size=font_size)


def show_menu(screen, action):
    show = True
    menu_background = pygame.image.load(os.path.join(img_folder, 'фон меню.png')).convert()
    start_button = Button(300, 70)
    quit_button = Button(350, 70)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(menu_background, (0, 0))
        start_button.draw(screen, 185, 230, 'Начать игру', action, 50)
        quit_button.draw(screen, 160, 320, 'Выйти из игры', quit, 50)
        pygame.display.update()
