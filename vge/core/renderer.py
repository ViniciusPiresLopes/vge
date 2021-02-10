import pygame


class Renderer:
    def __init__(self, surface, bg_color=(0, 0, 0)):
        self.surface = surface
        self.bg_color = bg_color
    
    def clear(self):
        self.surface.fill(self.bg_color)
    
    def display(self):
        pygame.display.flip()
