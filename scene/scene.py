from renderer.renderer import Renderer
from .camera import Camera
from .composite import Composite
from .scene_object import SceneObject


class Scene:
    """
    Represents a game scene with objects.
    """

    def __init__(self, name: str = "Scene"):
        self.name = name
        self.root = Composite("SceneRoot")
        self.camera = Camera()
        self.physics_engine = None

    def add_object(self, obj: SceneObject) -> None:
        """
        Adds an object to the scene.
        """
        self.root.add(obj)

    def remove_object(self, obj: SceneObject) -> None:
        """
        Removes an object from the scene.
        """
        self.root.remove(obj)

    def update(self, delta_time: float) -> None:
        """
        Updates the state of all objects in the scene.
        """
        if self.physics_engine:
            self.physics_engine.simulate(delta_time)

        self.root.update(delta_time)

    def render(self, renderer: Renderer) -> None:
        """
        Renders all objects in the scene.
        """
        if renderer:
            renderer.begin_scene(self)
            self.root.render(renderer)
            renderer.end_scene()
