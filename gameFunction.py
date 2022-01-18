import sys
import pygame

from brick import Brick


def check_keydown_events(event, platForm):
    if event.key == pygame.K_LEFT:
        platForm.moving_left = True
    if event.key == pygame.K_RIGHT:
        platForm.moving_right = True


def check_keyup_events(event, platForm, ball):
    if event.key == pygame.K_LEFT:
        platForm.moving_left = False
    if event.key == pygame.K_RIGHT:
        platForm.moving_right = False
    if event.key == pygame.K_UP:
        ball.start = False


def check_play_button(screen, bricks, platForm, ball, settings, gameStats, button, mouse_x, mouse_y):
    if button.rect.collidepoint(mouse_x, mouse_y):
        gameStats.reset_stats()
        gameStats.game_active = True
        bricks.empty()
        create_wall(screen, bricks, settings)
        platForm.platform_center()
        ball.ball_center()


def check_events(screen, bricks, platForm, ball, settings, gameStats, button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, platForm)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, platForm, ball)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, bricks, platForm, ball, settings, gameStats, button, mouse_x, mouse_y)


def create_wall(screen, bricks, settings):
    available_space_x = settings.width - 2 * settings.brick_width
    available_space_y = settings.height / 2 - settings.brick_height
    rows_number = int(available_space_y / (10 + settings.brick_height))
    brick_number = int(available_space_x / (10 + settings.brick_width))
    for i in range(rows_number):
        y = settings.brick_height + (settings.brick_height + 10) * i
        for j in range(brick_number):
            brick = Brick(screen, settings)
            brick.x = settings.brick_width + (settings.brick_width + 10) * j
            brick.y = y
            brick.rect.x = brick.x
            brick.rect.y = brick.y
            bricks.add(brick)


def game_over(gameStats):
    gameStats.game_active = False


def check_game_over(ball, gameStats):
    if ball.rect.bottom > ball.screen_rect.bottom:
        game_over(gameStats)


def update_screen(settings, screen, platForm, ball, bricks, gameStats, button):
    screen.fill(settings.bg_color)
    platForm.blitme()
    ball.blitme()
    bricks.draw(screen)
    if not gameStats.game_active:
        button.draw_button()
    pygame.display.flip()
