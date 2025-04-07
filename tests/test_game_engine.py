import pytest
from game.game_engine import GameEngine
from scene.scene import Scene
from renderer.opengl_renderer import OpenGLRenderer
from physics.box_2d_physics import Box2DPhysics

class TestGameEngine:
    @pytest.fixture
    def game_engine(self):
        """Fixture to create a fresh GameEngine instance for each test."""
        return GameEngine()

    def test_initialization(self, game_engine):
        """Test that GameEngine can be properly initialized."""
        result = game_engine.initialize(800, 600, "Test Game")
        assert result is True
        assert isinstance(game_engine.physics_engine, Box2DPhysics)
        assert isinstance(game_engine.renderer, OpenGLRenderer)

    def test_create_scene(self, game_engine):
        """Test scene creation functionality."""
        scene = game_engine.create_scene("TestScene")
        assert scene.name == "TestScene"
        assert scene in game_engine.scenes.values()
        assert game_engine.current_scene == scene

        # Create another scene and verify it doesn't change current_scene
        scene2 = game_engine.create_scene("AnotherScene")
        assert game_engine.scenes["AnotherScene"] == scene2
        assert game_engine.current_scene == scene  # still the first scene

    def test_set_current_scene(self, game_engine):
        """Test the ability to change the current scene."""
        scene1 = game_engine.create_scene("Scene1")
        scene2 = game_engine.create_scene("Scene2")

        assert game_engine.current_scene == scene1

        # Change current scene
        result = game_engine.set_current_scene("Scene2")
        assert result is True
        assert game_engine.current_scene == scene2

        # Try to set a non-existent scene
        result = game_engine.set_current_scene("NonExistentScene")
        assert result is False
        assert game_engine.current_scene == scene2  # unchanged

    def test_run_method_preconditions(self, game_engine):
        """Test that run method checks for required components."""
        # No current_scene, renderer or physics_engine yet
        game_engine.run()  # Should exit early without exceptions

        game_engine.create_scene("TestScene")
        game_engine.run()  # Still exit early, needs renderer and physics_engine

        # Initialize fully
        game_engine.initialize()
        # We don't actually run the game loop here, just check it can start