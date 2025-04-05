from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects.sprite import Sprite
    from scene.scene import Scene
else:
    Scene = Any
    Sprite = Any


class Renderer(ABC):
    """
    Abstract base class for rendering engine
    """

    def __init__(self):
        self.clear_color = (0, 0, 0, 255)  # black
        self.debug_mode = False

    @abstractmethod
    def begin_scene(self, scene: 'Scene') -> None:
        """
        Abstract method to start rendering a scene
        """
        pass

    @abstractmethod
    def end_scene(self) -> None:
        """
        Abstract method to end rendering a scene
        """
        pass

    @abstractmethod
    def draw_sprite(self, sprite: 'Sprite') -> None:
        """
        Abstract method to render a sprite
        """
        pass

    @abstractmethod
    def draw_collider(self, collider: Any) -> None:
        """
        Draw a collider for debug purposes
        """
        pass

    @abstractmethod
    def render_scene(self, scene: 'Scene') -> None:
        """
        Abstract method to render the entire scene
        """
        pass