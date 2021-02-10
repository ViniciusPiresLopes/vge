import pygame
from .node import Node
from .ids import MUSIC


class Music(Node):
    def __init__(self, music_path, **kwargs):
        super(Music, self).__init__(id=kwargs.get("id", MUSIC))
        self.music_path = music_path
    
    def play(self, loops=1):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(loops)
    
    def stop(self):
        pygame.mixer.music.stop()
    
    def pause(self):
        pygame.mixer.music.pause()
    
    def resume(self):
        pygame.mixer.music.unpause()
    
    def set_volume(self, value):
        pygame.mixer.music.set_volume(value)
    
    def get_volume(self):
        return pygame.mixer.music.get_volume()
