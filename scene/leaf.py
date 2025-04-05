from game_objects import GameObject
from renderer import Renderer
from .scene_object import SceneObject


class Leaf(SceneObject):
    """
    Class that represents a leaf node in the scene.
    """

    def __init__(self, name: str = "Leaf", game_object: GameObject = None):
        super().__init__(name)
        self.game_object = game_object

    def add(self, child: SceneObject) -> None:
        """
        Add operation is not supported for leaf objects
        """
        raise NotImplementedError("Cannot add child to a Leaf object")

    def remove(self, child: SceneObject) -> None:
        """
        Remove operation is not supported for leaf objects
        """
        raise NotImplementedError("Cannot remove child from a Leaf object")

    def update(self, delta_time: float) -> None:
        """
        Update the game object
        """
        if not self.enabled or not self.game_object:
            return

        self.game_object.update(delta_time)

    def render(self, renderer: Renderer) -> None:
        """
        Render the game object
        """
        if not self.enabled or not self.game_object:
            return

        self.game_object.render(renderer)
