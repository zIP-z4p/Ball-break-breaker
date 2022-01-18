from pygame import Surface


class PlatForm:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.image = Surface((100, 10))
        self.image.fill(self.settings.plat_color)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.plat_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.settings.plat_speed
        self.rect.centerx = self.center

    def platform_center(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

