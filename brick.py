import pygame

from pygame.sprite import Sprite


class Brick(Sprite):
    def __init__(self, screen, settings):
        super(Brick, self).__init__()

        self.screen = screen
        self.settings = settings

        self.image = pygame.Surface((self.settings.brick_width, self.settings.brick_height))
        self.image.fill(self.settings.brick_color)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

