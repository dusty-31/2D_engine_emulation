from .game_object import GameObject
from renderer.renderer import Renderer


class Sprite(GameObject):
    """
    Represents a 2D sprite in the game engine.
    """

    def __init__(self, name: str = "Sprite", texture_path: str = ""):
        super().__init__(name)
        self.texture_path = texture_path
        self.texture = None
        self.width = 0
        self.height = 0
        self.color = (255, 255, 255, 255)  # RGBA format

    def load_texture(self) -> bool:
        """
        Loads the texture from the specified path.
        """
        print(f"Loading texture from {self.texture_path}")
        # Simulate loading a texture
        self.width = 100
        self.height = 100
        self.texture = f"Texture loaded from {self.texture_path}"
        return True

    def update(self, delta_time: float) -> None:
        """
        Update the sprite's position based on its velocity.
        """
        if not self.enabled:
            return

        # Update position based on velocity
        self.transform.position += self.velocity * delta_time

    def render(self, renderer: Renderer) -> None:
        """
        Render the sprite using the provided renderer class.
        """
        if not self.enabled or not self.texture:
            return

        renderer.draw_sprite(self)
