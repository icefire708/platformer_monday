import pygame
from character import Character
from key_controller import Key_controller




def main() -> None:
    clock =  pygame.time.Clock()
    FPS = 60
    screen = pygame.display.set_mode((800, 1000))
    print('Game started!')
    player = Character((100, 400), image='character_view.png')
    handler = Key_controller(player)
    player.attack()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                handler.key_down(event.key)



        screen.fill((0, 0, 0))
        player.move_and_show(screen)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
