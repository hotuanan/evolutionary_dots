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
myfont = pygame.font.SysFont("Comic Sans MS", 30)
label = None
screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock() 
goal = Target()
p = Population(population_size=400, max_dot_steps=400)
ob = Obstacle(400, 20, WIDTH/2, HEIGHT/2)

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    goal.show()
    ob.show()
    if label is not None:
        screen.blit(label, (50, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    p.update(goal.rect)
    p.collision_with(rect=goal.rect, is_goal=True)
    p.collision_with(rect=ob.rect, is_goal=False)
    if p.all_dots_dead():
        p.calculate_fitness(goal=goal.rect)
        p.natural_selection()
        p.mutate_descendants(mutation_rate=0.1)
        print('Generation: {}\nBest fitness: {}'.format(p.gen, p.best_fitness))
        label = myfont.render('Generation: {}, Best Fitness: {}'.format(p.gen, p.best_fitness), 1, BLACK)
        # if p.best_fitness > best_fit:
        #     best_fit = p.best_fitness
        #     best_dot = p.best_dot
        p.gen += 1
    p.show()
    pygame.display.update()



    