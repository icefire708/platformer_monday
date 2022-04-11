import pygame
from character import Character
from key_controller import Key_controller


class Location:
    def __init__(self, size) -> None:
        self.side = 50
        self.dd = []
        self.w, self.h = size
        self.w, self.h = self.w // self.side, self.h // self.side
        self.dd.append('#' * self.w)
        for _ in range(self.h - 4):
            self.dd.append('#' + '.' * (self.w - 2) + '#')
            
        self.dd.append('#' + '.' * (self.w - 7) + '######')
        self.dd.append('#' + '.' * (self.w - 5) + '####')
        self.dd.append('#' * self.w)

    def draw(self, screen):
        cveta = {
            '#': (255, 0, 0),
            '.': (0, 0, 0)
        }
        for row in range(self.h):
            for col in range(self.w):
                pygame.draw.rect(screen, cveta[self.dd[row][col]], 
                (col * self.side, row * self.side, self.side, self.side))
                    
    def check_x(self, x_start, w, y_up, h, direction):
        if direction == 0:
            return x_start
        if direction == 1:
            left = x_start // self.side
            right = (x_start + w) // self.side
            up = y_up // self.side
            down = (y_up + h) // self.side
            for col in range(left, right + 1):
                for row in range(up, down):
                    if self.dd[row][col] != '.':
                        return col * self.side
            return x_start + w
        if direction == -1:
            pass # тут должен начать появляться код
        raise Exception('Неверное направление')

def main() -> None:
    clock =  pygame.time.Clock()
    FPS = 60
    screen = pygame.display.set_mode((800, 1000))
    current_location = Location(screen.get_size())
    print('Game started!')
    player = Character((100, 400), image='character_view.png')
    handler = Key_controller(player)
    # player.attack()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                handler.key_down(event.key)

        current_location.draw(screen)
        player.move_and_show(screen, current_location)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
