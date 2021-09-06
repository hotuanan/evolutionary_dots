import pygame
import random
from dot import Dot

class Population():
    def __init__(self, population_size: int=100, max_dot_steps: int=400) -> None:
        self.w, self.h = pygame.display.get_surface().get_size()
        self.dots = [Dot(max_steps=max_dot_steps) for _ in range(population_size)]
        self.dots_alive = population_size
        self.fitness_sum = 0
        self.gen = 0
        self.best_dot = None
        self.best_dot_steps = max_dot_steps
        self.best_fitness = 0

    def update(self, goal) -> None:
        for dot in self.dots:
            if dot.dead or dot.in_finish: 
                continue
            dot.move()
            #TODO Maybe increase the self best dot steps threshold 
            if dot.brain.step > self.best_dot_steps:
                if dot.collision_with(goal):
                    dot.in_finish = True
                else:
                    dot.dead = True
            if dot.dead or dot.in_finish:
                self.dots_alive -= 1            
        self.check_if_out_of_bounds()

    def all_dots_dead(self) -> bool:
        return self.dots_alive == 0

    def show(self) -> None:
        for dot in self.dots:
            dot.show()

    def check_if_out_of_bounds(self) -> None:
        for dot in self.dots:
            if dot.dead or dot.in_finish:
                continue
            if not dot.collision_with(pygame.Rect(5, 5, self.w - 5, self.h - 5)):
                dot.dead = True
                self.dots_alive -= 1


    def collision_with(self, rect: pygame.Rect, is_goal: bool) -> None:
        for dot in self.dots:
            if dot.dead or dot.in_finish:
                continue
            if is_goal:
                dot.in_finish = dot.collision_with(rect)
            else:
                dot.dead = dot.collision_with(rect)
            if dot.dead or dot.in_finish:
                self.dots_alive -= 1

    def calculate_fitness(self, goal: pygame.Rect) -> None:
        self.fitness_sum = 0
        self.best_fitness = 0
        self.best_dot = None
        for dot in self.dots:
            dot.calculate_fitness(goal)
            self.fitness_sum += dot.fitness
            if dot.fitness > self.best_fitness:
                self.best_fitness = dot.fitness
                if dot.in_finish:
                    self.best_dot_steps = dot.brain.step
                self.best_dot = dot.create_descendant()
        self.best_dot.champion = True
    
    def natural_selection(self) -> None:
        best_parent = self.select_parent()
        self.dots_alive = len(self.dots)
        self.dots = [best_parent.create_descendant() for _ in range(self.dots_alive)]
        self.dots[0] = self.best_dot

    def mutate_descendants(self, mutation_rate: float=0.01) -> None:
        for i in range(1, len(self.dots)):
            # if self.gen < 25:
            #     self.dots[i].mutate(0.5)
            # elif self.gen < 50:
            #     self.dots[i].mutate(0.25)
            # else:
            #     self.dots[i].mutate(0.01)
            self.dots[i].mutate(0.01)

    def select_parent(self) -> Dot:
        r = random.uniform(0, self.fitness_sum)
        current_running_fitness = 0
        for dot in self.dots:
            current_running_fitness += dot.fitness
            if current_running_fitness > r:
                return dot
