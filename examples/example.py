from vge.core.engine import Engine
from vge.core.scene import Scene
from vge.nodes.sprite import Sprite
from vge.nodes.moveable import Moveable
from vge.nodes.animated_sprite import AnimatedSprite
from vge.nodes.timer import Timer
from vge.nodes.camera import Camera
from vge.core.window import WindowConfig
from vge.core.input import MouseInput, KeyInput, Keys
WindowConfig.set("width", 1280)
WindowConfig.set("height", 720)
WindowConfig.set("title", "This is a example!")


class MainScene(Scene):
    def on_start(self):
        # Example moving the camera
        self.timer = Timer(2, True, True)

        self.camera = Camera(0, 0)
        self.player = Moveable(self.engine.window.width / 2, self.engine.window.height / 2, 1, 1)
        self.anim = AnimatedSprite([
            f"animation/Flower{i + 1}.png" for i in range(30)
        ], 15, x=0, y=0, scale_x=0.5, scale_y=0.5, origin_x=128, origin_y=128, flip_v=True)

        self.add_node("Timer", self.timer)
        self.add_node("Camera", self.camera)
        self.add_node("Player", self.player)
        self.player.add_node("Anim", self.anim)
        self.show_children_graph()

    def on_update(self):
        if self.timer.is_done():
            print(f"FPS: {self.engine.clock.get_fps()}")

        if KeyInput.is_pressed(Keys.K_W):
            self.camera.move(0, -5)
        if KeyInput.is_pressed(Keys.K_S):
            self.camera.move(0, 5)
        if KeyInput.is_pressed(Keys.K_A):
            self.camera.move(-5, 0)
        if KeyInput.is_pressed(Keys.K_D):
            self.camera.move(5, 0)
        
        if KeyInput.is_pressed(Keys.K_SPACE):
            self.player.scale.x += 0.1
            self.player.scale.y += 0.1


class MyGame(Engine):
    def on_start(self):
        self.add_scene("MainScene", MainScene)
        self.make_current_scene("MainScene")


if __name__ == "__main__":
    MyGame().run()
