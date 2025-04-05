from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from renderer.renderer import Renderer
else:
    Renderer = Any

from .transform import Transform
from .vector import Vector


class GameObject(ABC):
    """
    Base abstract class for game objects.
    """

    def __init__(self, name: str = "GameObject"):
        self.name = name
        self.transform = Transform()
        self.velocity = Vector()
        self.enabled = True

    @abstractmethod
    def update(self, delta_time: float) -> None:
        """
        Update the game object state.
        """
        pass

    @abstractmethod
    def render(self, renderer: 'Renderer') -> None:
        """
        Render the game object on the screen.
        """
        pass