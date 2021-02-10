from .node import Node
from .ids import MOVEABLE
from ..utils.vector import Vector2
from ..utils.globals import Global
from ..utils.last import Last


class Moveable(Node):
    def __init__(self, x=0, y=0, scale_x=1, scale_y=1, **kwargs):
        super(Moveable, self).__init__(id=kwargs.get("id", MOVEABLE))
        self.position = Vector2(x, y)
        self.scale = Vector2(scale_x, scale_y)
        self.globals = Global(self.position, self.scale)
        self.last = Last(self.position, self.scale, self.globals)
        self.origin = Vector2(kwargs.get("origin_x", 0), kwargs.get("origin_y", 0))
        self.scaled_origin = Vector2(self.origin.x, self.origin.y)
    
    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y
    
    def move(self, offset_x, offset_y):
        ts = self.get_timestep()
        eng_fps = self.scene.engine.fps_limit
        eng_fcs = 1 / eng_fps  # eng_fcs: Engine Frame Change in Seconds
        pixel_ratio = ts / eng_fcs
        converted_offset = Vector2(pixel_ratio * offset_x, pixel_ratio * offset_y)

        self.position.x += converted_offset.x
        self.position.y += converted_offset.y

    def update_global_variables(self):
        # Update last variables
        self.last.update_variables(self.position, self.scale, self.globals)

        # Update global variables
        current_parent = self.parent
        while not isinstance(current_parent, Moveable):
            if current_parent is None: break

            current_parent = current_parent.parent

        if current_parent is not None:
            self.globals.position.x = current_parent.globals.position.x + self.position.x
            self.globals.position.y = current_parent.globals.position.y + self.position.y
            self.globals.scale.x = current_parent.globals.scale.x * self.scale.x
            self.globals.scale.y = current_parent.globals.scale.y * self.scale.y
            self.scaled_origin.x = self.origin.x * self.globals.scale.x
            self.scaled_origin.y = self.origin.y * self.globals.scale.y

    def _update(self):
        self.update_global_variables()

        for node in self._nodes:
            node._update()
        
        self.on_update()
