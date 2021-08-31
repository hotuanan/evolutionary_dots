from typing_extensions import runtime
from obstacle import Obstacle
from population import Population
from target import Target
import pygame

WIDTH = 600
HEIGHT = 1200
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
FPS = 60

pygame.init()
clock = pygame.time.Clock() 
screen = pygame.display.set_mode((HEIGHT, WIDTH))
p = Population(population_size=400, max_dot_steps=400)
goal = Target()
ob = Obstacle(400, 20, WIDTH/2, HEIGHT/2)

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    goal.show()
    ob.show()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    p.update()
    if p.all_dots_dead():
        p.calculate_fitness(target=goal.rect)
        p.natural_selection()
        p.mutate_descendants(mutation_rate=0.1)
        print('Generation: {}\nBest fitness: {}'.format(p.gen, p.best_fitness))
        # if p.best_fitness > best_fit:
        #     best_fit = p.best_fitness
        #     best_dot = p.best_dot
        p.gen += 1
    else:
        p.collision_with(rect=ob.rect, is_goal=False)
        p.collision_with(rect=goal.rect, is_goal=True)
    p.show()
    pygame.display.update()



    