from .game_object import GameObject
from .vector import Vector
from renderer import Renderer


class PhysicsBody(GameObject):
    """
    Represents a physics body in the game engine.
    """

    def __init__(self, name: str = "PhysicsBody", mass: float = 1.0):
        super().__init__(name)
        self.mass = mass
        self.forces = Vector()
        self.physics_engine = None
        self.collider = None

    def update(self, delta_time: float) -> None:
        """
        Update the physics body state based on applied forces and mass.
        """

        if not self.enabled or not self.physics_engine:
            return

        # Acceleration calculation: F = ma => a = F/m
        acceleration = self.forces * (1.0 / self.mass) if self.mass > 0 else Vector()

        # Speed update: v = v0 + at
        self.velocity += acceleration * delta_time

        # Position update: p = p0 + vt
        self.transform.position += self.velocity * delta_time

        # Reset forces after applying them
        self.forces = Vector()

    def render(self, renderer: Renderer) -> None:
        """
        Render the physics body on the screen.
        """

        if not self.enabled:
            return

        if self.collider and renderer.debug_mode:
            renderer.draw_collider(self.collider)

    def apply_force(self, force: Vector) -> None:
        """
        Apply a force to the physics body.
        """

        self.forces += force
