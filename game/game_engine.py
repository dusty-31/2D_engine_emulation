from typing import Dict, Optional
import time

from physics import Box2DPhysics, PhysicsEngine
from renderer import OpenGLRenderer, Renderer
from scene.scene import Scene
from .resource_manager import ResourceManager
from .scripting_engine import ScriptingEngine


class GameEngine:
    """
    Main game engine class that manages scenes, rendering, and physics.
    """

    def __init__(self):
        self.scenes: Dict[str, Scene] = {}
        self.current_scene: Optional[Scene] = None
        self.physics_engine: Optional[PhysicsEngine] = None
        self.renderer: Optional[Renderer] = None
        self.resource_manager = ResourceManager()
        self.scripting_engine = ScriptingEngine()
        self.running = False
        self.delta_time = 0.0
        self.last_time = 0.0

    def initialize(self, width: int = 800, height: int = 600, title: str = "Game") -> bool:
        """
        Initializes the game engine with the specified window size and title.
        """

        print(f"Initializing game engine with window size: {width}x{height} and title: {title}")

        self.physics_engine = Box2DPhysics()
        self.renderer = OpenGLRenderer()

        if self.current_scene and self.current_scene.camera:
            self.current_scene.camera.viewport_width = width
            self.current_scene.camera.viewport_height = height

        return True

    def create_scene(self, name: str) -> Scene:
        """
        Creates a new scene with the specified name.
        """

        scene = Scene(name)
        self.scenes[name] = scene

        # If there's no current scene, set the new scene as the current one
        if not self.current_scene:
            self.current_scene = scene

        return scene

    def set_current_scene(self, name: str) -> bool:
        """
        Sets the current scene to the one with the specified name.
        """

        if name in self.scenes:
            self.current_scene = self.scenes[name]
            return True
        return False

    def run(self) -> None:
        """
        Runs the main game loop.
        """
        if not self.current_scene or not self.renderer or not self.physics_engine:
            print("Cannot run engine: scene, renderer or physics engine is not initialized")
            return

        self.running = True
        self.last_time = self._get_time()

        # Limit the number of iterations for demonstration purposes
        max_iterations = 10
        iteration_count = 0

        print("Starting game loop...")

        while self.running:
            current_time = self._get_time()
            # In demo mode, _get_time() returns 0.0, so delta_time is always 0
            # Setting a fixed value for the demonstration
            self.delta_time = 0.016  # +- 60 FPS
            self.last_time = current_time

            print(f"Frame {iteration_count + 1}: Updating scene...")
            self.current_scene.update(self.delta_time)

            print(f"Frame {iteration_count + 1}: Rendering scene...")
            self.renderer.render_scene(self.current_scene)

            self._process_input()

            # Limit the frame rate to 60 FPS
            time.sleep(0.016)  # +- 60 FPS

            iteration_count += 1
            if iteration_count >= max_iterations:
                print(f"Demo completed after {max_iterations} frames")
                self.running = False

            print("Game loop ended")

    def stop(self) -> None:
        """
        Stops the game engine.
        """
        self.running = False

    @staticmethod
    def _get_time() -> float:
        """
        Returns the current time in seconds.
        """

        return time.time()


    def _process_input(self) -> None:
        """
        Processes user input.
        This is a placeholder for actual input handling logic.
        """
        pass

    def _limit_fps(self, fps: int) -> None:
        """
        Limits the frame rate to the specified FPS.
        This is a placeholder for actual frame rate limiting logic.
        """
        pass
