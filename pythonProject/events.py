import pygame
import time
import sys
import os
import classes


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'pictures')
main_fon = pygame.image.load(os.path.join(img_folder, 'фон игровой.png'))  # основной фон


def all_events(player, screen, shots, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move_right = True
            elif event.key == pygame.K_a:
                player.move_left = True
            elif event.key == pygame.K_SPACE:
                new_shot = classes.SpiderWeb(screen, player)
                if (stats.score > 1000) and (stats.score <= 2000):
                    new_shot.speed -= 0.06
                elif (stats.score > 2000) and (stats.score >= 4000):
                    new_shot.speed -= 0.12
                elif stats.score > 4000 and (stats.score <= 6000):
                    new_shot.speed -= 0.17
                elif stats.score > 6000:
                    new_shot.speed -= 0.21
                shots.add(new_shot)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.move_right = False
            elif event.key == pygame.K_a:
                player.move_left = False


def update_screen(screen, player, shots, enemies, score):
    """Отрисовываем спрайты"""
    screen.blit(main_fon, (0, 0))
    score.show_score()
    for shot in shots.sprites():
        shot.draw()
    player.draw_player()
    enemies.draw(screen)
    pygame.display.flip()


def update_shots(shots, enemies, screen, stats, score):
    """Удаляем не нужные пули, логика столкновений"""
    shots.update()
    for shot in shots.copy():
        if shot.rect.bottom <= 0:
            shots.remove(shot)

    collisions = pygame.sprite.groupcollide(shots, enemies, True, True)
    if collisions:
        for i_enemy in collisions.values():
            stats.score += 20 * len(i_enemy)
        score.draw_image_score()
        check_record(stats, score)
        score.image_lifes()
    if len(enemies) == 0:
        shots.empty()
        create_enemies(screen, enemies)


def create_enemies(screen, enemies):
    for row_num in range(5):
        for i_enemy in range(11):
            enemy = classes.Fly(screen)
            enemy.x = enemy.rect.width + enemy.rect.width * i_enemy
            enemy.y = enemy.rect.height + enemy.rect.height * row_num
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.y
            enemies.add(enemy)


def update_enemies(enemies, player, screen, shots, stats, score):
    enemies.update()
    if pygame.sprite.spritecollideany(player, enemies):
        player_die(stats, screen, player, enemies, shots, score)
    check_line(enemies, player, screen, shots, stats, score)


def check_line(enemies, player, screen, shots, stats, score):
    for i_enemy in enemies.sprites():
        if i_enemy.rect.bottom >= screen.get_rect().bottom:
            player_die(stats, screen, player, enemies, shots, score)
            break


def player_die(stats, screen, player, enemies, shots, score):
    if stats.player_life > 0:
        stats.player_life -= 1
        score.image_lifes()
        enemies.empty()
        shots.empty()
        create_enemies(screen, enemies)
        player.create_player()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def check_record(stats, score):
    if stats.score > stats.record:
        stats.record = stats.score
        score.draw_record()
        with open('records.txt', 'w') as file:
            file.write(str(stats.record))
