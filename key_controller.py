import pygame

class Key_controller:
    def __init__(self, hero) -> None:
        self.hero = hero

    def key_down(self, key):
        if key == pygame.K_d:
            self.hero.set_direction('right')
        if key == pygame.K_a:
            self.hero.set_direction('left')
        if key == pygame.K_w:
            self.hero.jump()