import pygame
import gameFunction as gf

from pygame.sprite import Group

from settings import Settings
from platForm import PlatForm
from ball import Ball
from gameStats import GameStats
from button import Button
from allSound import MusicAndSound


def run_game():
    settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((settings.width, settings.height))
    pygame.display.set_caption("Ball and break")

    platForm = PlatForm(screen, settings)
    ball = Ball(screen, platForm, settings)
    gameStats = GameStats(settings)
    button = Button(settings, screen, "Play")
    musicAndSound = MusicAndSound()
    bricks = Group()

    gf.create_wall(screen, bricks, settings)

    clock = pygame.time.Clock()

    while True:
        clock.tick(settings.FPS)
        gf.check_events(screen, bricks, platForm, ball, settings, gameStats, button)
        if gameStats.game_active:
            platForm.update()
            ball.update(bricks, musicAndSound)
            gf.check_game_over(ball, gameStats)
        gf.update_screen(settings, screen, platForm, ball, bricks, gameStats, button)


run_game()
