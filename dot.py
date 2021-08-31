from brain import Brain
import pygame
import math


class Dot(pygame.sprite.Sprite):
    def __init__(self, max_steps: int=400) -> None:
        self.screen = pygame.display.get_surface()
        self.w, self.h = self.screen.get_size()
        self.image = pygame.Surface((5, 5))  # The tuple represent size. 
        self.rect = self.image.get_rect(center=(self.w/10, self.h/2))
        self.brain = Brain(max_steps)
        self.velocity = [0, 0]
        self.fitness = 0
        self.champion = False
        self.in_finish = False
        self.dead = False
        pass
    
    def __limit_velocity__(self, max: int=20) -> None:
        magnitudeSq = self.velocity[0] ** 2 + self.velocity[1]**2 
        if magnitudeSq < max ** 2:
            return
        self.velocity[0] /= math.sqrt(magnitudeSq)
        self.velocity[1] /= math.sqrt(magnitudeSq)

    def move(self) -> None:
        acceleration = self.brain.get_acceleration()
        if acceleration is None:
            self.dead = True
            return
        self.velocity[0] += acceleration[0]
        self.velocity[1] += acceleration[1]
        self.__limit_velocity__()
        self.rect.move_ip(*self.velocity) # asterisk makes from: method([0, 0]) to method(0, 0)

    def collision_with(self, rect: pygame.Rect) -> bool:
        return self.rect.colliderect(rect)

    def calculate_fitness(self, target: pygame.Rect):
        if self.in_finish:
            self.fitness = 100 + 100/(self.brain.step + 1)
        else:
            dist = (self.rect.x - target.x)**2 + (self.rect.y - target.y)**2
            self.fitness = 100/(dist + 1)
        
    
    def mutate(self, mutation_rate: float=0.01) -> None:
        self.brain.mutate(mutation_rate=mutation_rate)

    def create_descendant(self) -> 'Dot':
        desc = Dot()
        desc.brain.directions = self.brain.directions.copy()
        return desc

    def show(self) -> None:
        if self.champion:
            self.image.fill((0, 0, 255))
        self.screen.blit(self.image, self.rect)