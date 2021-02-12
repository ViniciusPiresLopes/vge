import pygame
from .moveable import Moveable
from .ids import SPRITE


class Sprite(Moveable):
    def __init__(self, img_path, **kwargs):
        super(Sprite, self).__init__(
            kwargs.get("x", 0), kwargs.get("y", 0), 
            kwargs.get("scale_x", 1), kwargs.get("scale_y", 1), 
            origin_x=kwargs.get("origin_x", 0), origin_y=kwargs.get("origin_y", 0),
            id=kwargs.get("id", SPRITE)
        )
        self.surface = pygame.image.load(img_path)
        self.surface_width = self.surface.get_width()
        self.surface_height = self.surface.get_height()
        self.scaled_surface = self.surface
        self.scaled_surface_width = self.surface_width
        self.scaled_surface_height = self.surface_height
        self.flip_h = kwargs.get("flip_h", False)
        self.flip_v = kwargs.get("flip_v", False)
        self.visible = True
    
    def on_start(self):
        pass
    
    def show(self):
        self.visible = True
    
    def hide(self):
        self.visible = False
    
    def _draw(self):
        if self.visible and self.surface is not None:
            # Flip image
            self.flipped_surface = self.surface
            if self.flip_h or self.flip_v:
                self.flipped_surface = pygame.transform.flip(self.surface, self.flip_h, self.flip_v)

            # Scale image
            self.scaled_surface_width = round(self.surface_width * self.global_.get("scale").x)
            self.scaled_surface_height = round(self.surface_height * self.global_.get("scale").y)
            self.scaled_surface = pygame.transform.scale(self.flipped_surface, (self.scaled_surface_width, self.scaled_surface_height))

            # Draw image
            position_x = self.global_.get("position").x - self.scaled_origin.x
            position_y = self.global_.get("position").y - self.scaled_origin.y
            self.scene.engine.window.surface.blit(self.scaled_surface, (position_x, position_y))
    
    def on_update(self):
        self._draw()
