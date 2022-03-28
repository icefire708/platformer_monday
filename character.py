import pygame

class Character:
    def __init__(self, coords: tuple, image=None, w=100, h=200) -> None:
        self.HP = 10
        self.x, self.y = coords
        self.w, self.h = w, h
        self.direction = 0
        self.velocity = 10 # горизонтальная
        self.jump_speed = 0
        if image:
            self.view = pygame.transform.scale(pygame.image.load(image), (w, h))
        else:
            self.view = None

    def attack(self) -> None:
        print('Я атаковал!!!')

    def move_and_show(self, screen) -> None:
        self.x += self.direction * self.velocity
        # self.y += self.jump_speed
        # if self.jump_speed:
        #     self.jump_speed += 15
        screen.blit(self.view, (self.x - self.w//2, self.y - self.h//2))

    def set_direction(self, dir):
        if dir == 'left':
            self.direction = -1
        elif dir == 'right':
            self.direction = 1
        elif dir == 'stay':
            self.direction = 0 # прямо
    
    def jump(self):
        self.jump_speed = -100