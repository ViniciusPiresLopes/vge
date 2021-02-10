from .vector import Vector2


class Global:
    def __init__(self, position, scale):
        self.position = Vector2(position.x, position.y)
        self.scale = Vector2(scale.x, scale.y)
