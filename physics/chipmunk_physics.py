from .physics_engine import PhysicsEngine


class ChipmunkPhysics(PhysicsEngine):
    """
    Implementation of the Chipmunk physics engine
    """

    def __init__(self):
        super().__init__()
        print("Initializing Chipmunk Physics Engine")

    def simulate(self, delta_time: float) -> None:
        """
        Simulates the physics using Chipmunk
        """
        print(f"Simulating Chipmunk physics for {len(self.physics_objects)} objects")
