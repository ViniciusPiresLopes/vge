from .vector import Vector2
from .globals import Global


class Last:
    def __init__(self, position, scale, globals):
        self.position = Vector2(position.x, position.y)
        self.scale = Vector2(scale.x, scale.y)
        self.globals = Global(globals.position, globals.scale)
    
    def update_variables(self, position, scale, globals):
        self.position.x = position.x
        self.position.y = position.y
        self.scale.x = scale.x
        self.scale.y = scale.y
        self.globals.position.x = globals.position.x
        self.globals.position.y = globals.position.y
        self.globals.scale.x = globals.scale.x
        self.globals.scale.y = globals.scale.y
