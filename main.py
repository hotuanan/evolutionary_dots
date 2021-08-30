from typing_extensions import runtime
from dot import Dot
import pygame

WIDTH = 600
HEIGHT = 1200
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
FPS = 60

pygame.init()
clock = pygame.time.Clock() 
screen = pygame.display.set_mode((HEIGHT, WIDTH))
d = Dot(screen=screen)

running = True
while running:
    dt = clock.tick(FPS) / 1000
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # elif event.type == pygame.KEYDOWN: 
        #     if event.key == pygame.K_w: 
        #         d.velocity[1] = -200 * dt
        #     elif event.key == pygame.K_s: 
        #         d.velocity[1] = 200 * dt
        #     elif event.key == pygame.K_a: 
        #         d.velocity[0] = -200 * dt
        #     elif event.key == pygame.K_d: 
        #         d.velocity[0] = 200 * dt
        # elif event.type == pygame.KEYUP: 
        #     if event.key == pygame.K_w or event.key == pygame.K_s: 
        #         d.velocity[1] = 0 
        #     elif event.key == pygame.K_a or event.key == pygame.K_d: 
        #         d.velocity[0] = 0 
    d.update()
    d.show()
    pygame.display.update()

    