from typing import DefaultDict
import pygame
import random
from dot import Dot

class Population():
    def __init__(self, population_size: int=100, max_dot_steps: int=400):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.dots = [Dot(max_steps=max_dot_steps) for _ in range(population_size)]
        self.dots_alive = population_size
        self.fitness_sum = 0
        self.gen = 0
        self.best_dot = None
        self.best_dot_steps = max_dot_steps
        self.best_fitness = 0

    def update(self):
        for dot in self.dots:
            if dot.dead or dot.in_finish: 
                continue
            dot.move()
            if dot.brain.step > self.best_dot_steps:
                dot.dead = True
            # runs out of moves
            if dot.dead:
                self.dots_alive -= 1
        self.check_if_out_of_bounds()

    def all_dots_dead(self):
        return self.dots_alive == 0

    def show(self):
        for dot in self.dots:
            dot.show()

    def check_if_out_of_bounds(self):
        for dot in self.dots:
            if dot.dead:
                continue
            if not dot.collision_with(pygame.Rect(5, 5, self.w - 10, self.h - 10)):
                dot.dead = True
                self.dots_alive -= 1


    def collision_with(self, rect: pygame.Rect, is_goal: bool):
        for dot in self.dots:
            if dot.dead or dot.in_finish:
                continue
            if dot.collision_with(rect):
                if is_goal:
                    dot.in_finish = True
                else:
                    dot.dead = True
                self.dots_alive -= 1

    def calculate_fitness(self, target: pygame.Rect):
        self.best_fitness = 0
        self.best_dot = None
        for dot in self.dots:
            dot.calculate_fitness(target)
            # self.fitness_sum += dot.fitness
            if dot.fitness > self.best_fitness:
                self.best_fitness = dot.fitness
                if dot.in_finish:
                    self.best_dot_steps = dot.brain.step
                self.best_dot = dot.create_descendant()
        self.best_dot.champion = True
    
    def calc_fitness_sum(self):
        self.fitness_sum = 0
        for dot in self.dots:
            self.fitness_sum += dot.fitness

    def natural_selection(self):
        self.calc_fitness_sum()
        best_parent = self.select_parent()
        self.dots_alive = len(self.dots)
        self.dots = [best_parent.create_descendant() for _ in range(self.dots_alive)]
        self.dots[0] = self.best_dot

    def mutate_descendants(self):
        for i in range(1, len(self.dots)):
            self.dots[i].mutate()

    def select_parent(self) -> Dot:
        #TODO - find a good parent selecting function
        r = random.uniform(0, self.fitness_sum)
        current_running_fitness = 0
        for dot in self.dots:
            current_running_fitness += dot.fitness
            if current_running_fitness > r:
                return dot
