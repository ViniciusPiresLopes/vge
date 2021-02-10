import pygame
pygame.init()

from .window import Window, WindowConfig, PygameWindowConfig
from .renderer import Renderer
from .input import MouseInput, KeyInput


class Engine:
    def __init__(self, **kwargs):
        self.fps_limit = kwargs.get("fps_limit", 60)
        self.window = Window(
            width=WindowConfig.get("width"),
            height=WindowConfig.get("height"),
            title=WindowConfig.get("title"),
        )
        self.renderer = Renderer(self.window.surface)
        self.clock = pygame.time.Clock()
        self.timestep = 0

        self.scenes = {}
        self.current_scene = None

        self.running = False

        self.on_start()
    
    def on_start(self):
        pass
    
    def add_scene(self, name, scene_ref):
        self.scenes[name] = scene_ref
    
    def make_current_scene(self, name):
        self.current_scene = self.scenes[name](engine=self)
        self.current_scene.on_start()
    
    def get_timestep(self):
        return self.timestep
    
    def _update(self):
        if self.current_scene is not None:
            self.current_scene._update()
        
        MouseInput._update()
        KeyInput._update()
    
    def run(self):
        self.running = True

        while self.running:
            self.timestep = self.clock.tick(self.fps_limit) / 1000
            # Just for test, will be removed from here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.renderer.clear()
            self._update()
            self.renderer.display()
        
        pygame.quit()
