from .physics_engine import PhysicsEngine


class Box2DPhysics(PhysicsEngine):
    """
    Implementation of the Box2D physics engine
    """

    def __init__(self):
        super().__init__()
        print("Initializing Box2D Physics Engine")

    def simulate(self, delta_time: float) -> None:
        """
        Simulates the physics using Box2D
        """
        for obj in self.physics_objects:
            gravity_force = self.gravity * obj.mass
            obj.apply_force(gravity_force)

        self._detect_collisions()
        for obj in self.physics_objects:
            obj.update(delta_time)

    def _detect_collisions(self) -> None:
        """
        Detects collisions between physics objects
        """
        # Simple collision detection logic
        for i in range(len(self.physics_objects)):
            for j in range(i + 1, len(self.physics_objects)):
                obj1 = self.physics_objects[i]
                obj2 = self.physics_objects[j]

                print(f"Checking collision between {obj1.name} and {obj2.name}")
