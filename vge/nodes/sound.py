import pygame
from .node import Node
from .ids import SOUND


class Sound(Node):
    def __init__(self, sound_path, **kwargs):
        super(Sound, self).__init__(id=kwargs.get("id", SOUND), **kwargs)
        self.sound_path = sound_path
        self.sound = pygame.mixer.Sound(self.sound_path)
        self.channel = None
    
    def play(self, loops=1):
        self.channel = self.sound.play(loops)
    
    def stop(self):
        self.sound.stop()
    
    def set_volume(self, value):
        self.sound.set_volume(value)
    
    def get_volume(self):
        self.sound.get_volume()
    
    def has_ended(self):
        if self.channel is None:
            return True
        
        return not self.channel.get_busy()
