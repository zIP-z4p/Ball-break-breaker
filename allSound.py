import pygame


class MusicAndSound:
    pygame.mixer.init()

    def __init__(self):
        self.soundBallHit = pygame.mixer.Sound("audio/ball_hit.wav")
