from typing import Any, TYPE_CHECKING

from .renderer import Renderer
from game_objects.sprite import Sprite

if TYPE_CHECKING:
    from scene.scene import Scene
else:
    Scene = Any


class DirectXRenderer(Renderer):
    """
    Implementation of a renderer based on DirectX
    """

    def __init__(self):
        super().__init__()
        print("Initializing DirectX Renderer")
        # Placeholder for DirectX initialization

    def begin_scene(self, scene: 'Scene') -> None:
        """
        Starts rendering a scene using DirectX
        """

        print(f"Beginning scene rendering with DirectX: {scene.name}")

    def end_scene(self) -> None:
        """
        Ends rendering a scene using DirectX
        """

        print("Ending scene rendering with DirectX")

    def draw_sprite(self, sprite: Sprite) -> None:
        """
        Renders a sprite using DirectX
        """

        print(f"Drawing sprite with DirectX: {sprite.name}")

    def draw_collider(self, collider: Any) -> None:
        """
        Renders a collider for debugging purposes using DirectX
        """

        print(f"Drawing collider with DirectX for debug purposes")

    def render_scene(self, scene: Scene) -> None:
        """
        Renders the entire scene using DirectX
        """

        self.begin_scene(scene)
        scene.render(self)
        self.end_scene()
