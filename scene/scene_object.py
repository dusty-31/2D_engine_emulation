from abc import ABC, abstractmethod

from renderer import Renderer


class SceneObject(ABC):
    """
    Base abstract class for scene objects.
    """

    def __init__(self, name: str = "SceneObject"):
        self.name = name
        self.enabled = True

    @abstractmethod
    def add(self, child: 'SceneObject') -> None:
        """
        Adds a child object to the scene object.
        """
        pass

    @abstractmethod
    def remove(self, child: 'SceneObject') -> None:
        """
        Removes a child object from the scene object.
        """
        pass

    @abstractmethod
    def update(self, delta_time: float) -> None:
        """
        Update the scene object and its children.
        """
        pass

    @abstractmethod
    def render(self, renderer: Renderer) -> None:
        """
        Renders the scene object and its children.
        """
        pass
