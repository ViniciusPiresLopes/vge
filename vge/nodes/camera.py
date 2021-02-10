from .moveable import Moveable
from .ids import CAMERA 
from ..utils.vector import Vector2


class Camera(Moveable):
    def __init__(self, x=0, y=0, follow_target=None, **kwargs):
        super(Camera, self).__init__(x, y, 1, 1, id=kwargs.get("id", CAMERA))
        self.follow_target = follow_target
    
    def follow(self, target):
        self.follow_target = target
    
    def on_update(self):
        self.scene.position.x = -self.position.x
        self.scene.position.y = -self.position.y
