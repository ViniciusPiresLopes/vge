from ..nodes.moveable import Moveable
from ..nodes.ids import SCENE
from ..utils.vector import Vector2


class Scene(Moveable):
    def __init__(self, **kwargs):
        super(Scene, self).__init__(0, 0, 1, 1, id=kwargs.get("id", SCENE))
        self.engine = kwargs.get("engine")
    
    def get_timestep(self):
        return self.engine.get_timestep()
    
    def add_node(self, name, node):
        self._nodes.append(node)
        self.nodes_ref[name] = self._nodes[-1]
        self._nodes[-1].name = name
        self._nodes[-1].scene = self
        self._nodes[-1].parent = self
        self._nodes[-1].on_start()
        
        return self._nodes[-1]

    def update_global_variables(self):
        self.global_.push("position", Vector2(
            self.position.x, self.position.y
        ))
