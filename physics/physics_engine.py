from abc import ABC, abstractmethod
from typing import List

from game_objects import PhysicsBody, Vector


class PhysicsEngine(ABC):
    """
    Abstract base class for a physics engine.
    """

    def __init__(self):
        self.gravity = Vector(0, 9.8)
        self.physics_objects: List[PhysicsBody] = []

    @abstractmethod
    def simulate(self, delta_time: float) -> None:
        """
        Simulate the physics for the given time step
        """
        pass

    def add_physics_object(self, obj: PhysicsBody) -> None:
        """
        Adds a physics object to the simulation
        """
        if obj not in self.physics_objects:
            self.physics_objects.append(obj)
            obj.physics_engine = self

    def remove_physics_object(self, obj: PhysicsBody) -> None:
        """
        Removes a physics object from the simulation
        """
        if obj in self.physics_objects:
            self.physics_objects.remove(obj)
            obj.physics_engine = None
