import pygame
from .sprite import Sprite
from .ids import ANIMATED_SPRITE
from ..utils.methods import clamp


class AnimatedSprite(Sprite):
    def __init__(self, images, anim_fps=None, **kwargs):
        super(AnimatedSprite, self).__init__(
            images[0], x=kwargs.get("x", 0), y=kwargs.get("y", 0), 
            scale_x=kwargs.get("scale_x", 1), scale_y=kwargs.get("scale_y", 1),
            origin_x=kwargs.get("origin_x", 0), origin_y=kwargs.get("origin_y", 0),
            flip_h=kwargs.get("flip_h", False), flip_v=kwargs.get("flip_v", False),
            id=ANIMATED_SPRITE
        )
        self.surfaces = []
        self.index = 0
        self.time = 0
        self.anim_fps = anim_fps
        if self.anim_fps is None: self.anim_fps = self.scene.engine.fps_limit

        for img in images:
            self.surfaces.append(pygame.image.load(img))
    
    def _advance(self):
        frames_count = len(self.surfaces)
        ts = self.get_timestep()

        eng_fps = self.scene.engine.fps_limit
        eng_fcs = 1 / eng_fps # eng_fcs -> engine frame change (in secs)
        anim_fcs = 1 / self.anim_fps # anim_fcs -> animation frame change (in secs)
        anim_ratio = anim_fcs / eng_fcs  # engine fps and animation fps can be different, anim_ratio makes the animation go at the right pace
        fcs = eng_fcs * anim_ratio # frame change (in secs)

        if self.time <= frames_count * fcs:
            self.time += ts
            self.index = clamp(int(self.time / fcs), 0, frames_count - 1)
            self.surface = self.surfaces[self.index]
        else:
            self.time = 0
            self.index = 0
            self.surface = self.surfaces[self.index]

    def on_update(self):
        self._draw()
        self._advance()
