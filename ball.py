import pygame


class Ball:

    def __init__(self, screen, platForm, settings):
        self.screen = screen
        self.platForm = platForm
        self.settings = settings

        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.platForm.rect.centerx
        self.rect.bottom = self.platForm.rect.centery - 5
        self.rebound = True

        self.start = True

    def rebound_border(self):
        if self.screen_rect.left > self.rect.left or self.screen_rect.right < self.rect.right:
            self.settings.ball_speed_x = -self.settings.ball_speed_x
            self.rebound = True
        if self.screen_rect.top > self.rect.top:
            self.settings.ball_speed_y = -self.settings.ball_speed_y
            self.rebound = True

    def rebound_platform(self):
        if (self.platForm.rect.left - 3 <= self.rect.centerx <= self.platForm.rect.right + 3 and
                self.rect.bottom > self.platForm.rect.top and self.rebound):
            self.settings.ball_speed_y = -self.settings.ball_speed_y
            self.rebound = False

    def rebound_brick(self, bricks, musicAndSound):
        collisions = pygame.sprite.spritecollide(self, bricks, True)
        if collisions:
            musicAndSound.soundBallHit.play()
            brick = collisions[0]
            if ((self.rect.bottom > brick.rect.top or self.rect.top < brick.rect.bottom) and
                (brick.rect.left < self.rect.centerx < brick.rect.right)):
                self.settings.ball_speed_y = - self.settings.ball_speed_y
            elif self.rect.left > brick.rect.left or self.rect.right < brick.rect.right:
                self.settings.ball_speed_x = - self.settings.ball_speed_x
            self.rebound = True

    def update(self, bricks, musicAndSound):
        if self.start:
            self.rect.centerx = self.platForm.rect.centerx
            self.rect.bottom = self.platForm.rect.centery - 5
        else:
            self.rebound_brick(bricks, musicAndSound)
            self.rebound_border()
            self.rebound_platform()
            self.rect.centerx -= self.settings.ball_speed_x
            self.rect.centery += self.settings.ball_speed_y

    def ball_center(self):
        self.rect.centerx = self.platForm.rect.centerx
        self.rect.bottom = self.platForm.rect.centery - 5
        self.rebound = True

        self.start = True

    def blitme(self):
        self.screen.blit(self.image, self.rect)
