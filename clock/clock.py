import pygame


class GameClock:
    clock = pygame.time.Clock()
    time_passed = 0

    @classmethod
    def update(cls):
        cls.clock.tick(500)
        cls.time_passed += cls.dt()

    @classmethod
    def dt(cls):
        return cls.clock.get_time() / 1000

    @classmethod
    def time(cls):
        return cls.time_passed
