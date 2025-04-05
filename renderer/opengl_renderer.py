from typing import Any

from .renderer import Renderer
from game_objects.sprite import Sprite
from scene import Scene


class OpenGLRenderer(Renderer):
    """
    Implementation of a renderer based on OpenGL
    """

    def __init__(self):
        super().__init__()
        print("Initializing OpenGL Renderer")
        # Placeholder for OpenGL initialization

    def begin_scene(self, scene: Scene) -> None:
        """
        Starts rendering a scene using OpenGL
        """

        print(f"Beginning scene rendering with OpenGL: {scene.name}")
        # clear the screen with the specified clear color
        r, g, b, a = self.clear_color
        print(f"Clearing screen with color: ({r}, {g}, {b}, {a})")

    def end_scene(self) -> None:
        """
        Ends rendering a scene using OpenGL
        """

        print("Ending scene rendering with OpenGL")

    def draw_sprite(self, sprite: Sprite) -> None:
        """
        Renders a sprite using OpenGL
        """

        sprite_position = f"{sprite.transform.position.x}, {sprite.transform.position.y}"
        print(f"Drawing sprite: {sprite.name} at position ({sprite_position})")

    def draw_collider(self, collider: Any) -> None:
        """
        Renders a collider for debugging purposes using OpenGL
        """

        print(f"Drawing collider for debug purposes")

    def render_scene(self, scene: Scene) -> None:
        """
        Renders the entire scene using OpenGL
        """

        self.begin_scene(scene)
        scene.render(self)
        self.end_scene()
