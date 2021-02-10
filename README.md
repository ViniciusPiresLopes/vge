# VGE
VGE (Vini Game Engine) is a 2D game engine made with pygame. It supports Scene and Nodes, each node with its facility.

## Instalation
Avaliable soon...

## Usage

```
from vge.core.engine import Engine
from vge.core.scene import Scene


class MyScene(Scene):
    def on_start(self):
        pass


class MyGame(Engine):
    def on_start(self):
        self.add_scene("MyScene", MyScene)
        self.make_current_scene("MyScene")


if __name__ == "__main__":
    MyGame().run()
```

## License
VGE is released under the MIT license. See LICENSE for details.
