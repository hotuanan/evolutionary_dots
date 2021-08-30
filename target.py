import pygame

class Target(pygame.sprite.Sprite):
    def __init__(self):
        w, h = pygame.display.get_surface().get_size()
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(w - 40, h/2))
    
    def show(self):
        pygame.display.get_surface().blit(self.image, self.rect)