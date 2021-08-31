import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, sizex, sizey, centerx, centery) -> None:
        w, h = pygame.display.get_surface().get_size()
        self.image = pygame.Surface((sizey, sizex + 400))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(centery - 5, centerx - 5 + 200))
    
    def show(self) -> None:
        pygame.display.get_surface().blit(self.image, self.rect)
