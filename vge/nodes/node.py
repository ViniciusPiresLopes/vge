"""
Methods with "on_" prefix, means that is a special method and can be replaced.
Methods with "_" prefix, means that is a private method and should not be replaced.
"""
from .ids import NODE


class Node:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", NODE)
        self.name = None
        self.scene = None
        self.parent = None
        self._nodes = []
        self.nodes_ref = {}
    
    def add_node(self, name, node):
        self._nodes.append(node)
        self.nodes_ref[name] = self._nodes[-1]
        self._nodes[-1].name = name
        self._nodes[-1].scene = self.scene
        self._nodes[-1].parent = self
        self._nodes[-1].on_start()

        return self._nodes[-1]
    
    def get_node(self, name):
        return self.nodes_ref.get(name)
    
    def get_timestep(self):
        return self.scene.engine.get_timestep()

    def on_start(self):
        """
        Use if you won't modify __init__ arguments.
        """
        pass

    def on_update(self):
        pass

    def _update(self):
        for node in self._nodes:
           node._update()
        
        self.on_update()
    
    def print_children_tree(self, **kwargs):
        tab = "  "
        space = tab * kwargs.get("current_time", 0)

        for child in self._nodes:
            print(end=space)
            print(f"-{child}")
            child.print_children_tree(current_time=kwargs.get("current_time", 0) + 1)

    
    def __repr__(self):
        return f"[{self.name}]:[{self.id}]"
