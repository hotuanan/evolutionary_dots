import pygame
import math

from pygame.draw import rect
from brain import Brain

class Dot(pygame.sprite.Sprite):
    def __init__(self, direction_size=400):
        self.screen = pygame.display.get_surface()
        self.w, self.h = self.screen.get_size()
        self.image = pygame.Surface((5, 5))  # The tuple represent size. 
        self.rect = self.image.get_rect(center=(self.w/2, self.h/2))
        self.brain = Brain(direction_size)
        self.velocity = [0, 0]
        self.dead = False
        pass
    
    def __limit_velocity__(self, max=10):
        magnitudeSq = self.velocity[0] ** 2 + self.velocity[1]**2 
        if magnitudeSq < max ** 2:
            return
        self.velocity[0] /= math.sqrt(magnitudeSq)
        self.velocity[1] /= math.sqrt(magnitudeSq)

    def __move__(self):
        acceleration = self.brain.get_acceleration()
        if acceleration is None:
            self.dead = True
            return
        self.velocity[0] += acceleration[0]
        self.velocity[1] += acceleration[1]
        self.__limit_velocity__()
        self.rect.move_ip(*self.velocity) # asterisk makes from: method([0, 0]) to method(0, 0)

    def update(self):
        if self.dead:
            return
        self.__move__()
        # if not in bounds
        if not pygame.Rect(0, 0, self.w - 5, self.h - 5).colliderect(self.rect):
            self.dead = True

    def show(self):
        self.screen.blit(self.image, self.rect)