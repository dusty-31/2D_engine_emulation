from typing import List

from renderer import Renderer
from .scene_object import SceneObject


class Composite(SceneObject):
    """
    Composite class that represents a group of scene objects.
    """
    def __init__(self, name: str = "Composite"):
        super().__init__(name)
        self.children: List[SceneObject] = []

    def add(self, child: SceneObject) -> None:
        """
        Adds a child object to the composite.
        """
        if child not in self.children:
            self.children.append(child)

    def remove(self, child: SceneObject) -> None:
        """
        Removes a child object from the composite.
        """
        if child in self.children:
            self.children.remove(child)

    def update(self, delta_time: float) -> None:
        """
        Update all child objects
        """
        if not self.enabled:
            return

        for child in self.children:
            child.update(delta_time)

    def render(self, renderer: Renderer) -> None:
        """
        Render all child objects
        """
        if not self.enabled:
            return

        for child in self.children:
            child.render(renderer)