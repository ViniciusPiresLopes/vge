import pygame


class PygameWindowConfig:
    config = {
    }

    @staticmethod
    def set(key, value):
        PygameWindowConfig.config[key] = value
    
    @staticmethod
    def get(key):
        return PygameWindowConfig.config.get(key)


class WindowConfig:
    config = {
        "width": 800, "height": 640, "title": "untitled"
    }

    @staticmethod
    def set(key, value):
        WindowConfig.config[key] = value
    
    @staticmethod
    def get(key):
        return WindowConfig.config.get(key)


class Window:
    def __init__(self, **kwargs):
        self.width = kwargs.get("width", WindowConfig.get("width"))
        self.height = kwargs.get("height", WindowConfig.get("heigh"))
        self.title = kwargs.get("title", WindowConfig.get("title"))
        self.surface = kwargs.get("surface")

        self.create_window() 
    
    def create_window(self):
        self.surface = pygame.display.set_mode((self.width, self.height), **PygameWindowConfig.config)
        pygame.display.set_caption(self.title)
    
    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.create_window()
    
    def set_title(self, title):
        self.title = title
        pygame.display.set_caption(self.title)
