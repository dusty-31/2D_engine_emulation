from .vector import Vector


class Transform:
    """
    A class representing a transformation with position, rotation, and scale.
    """
    def __init__(self, position: Vector = None, rotation: float = 0.0, scale: Vector = None):
        self.position = position if position else Vector()
        self.rotation = rotation
        self.scale = scale if scale else Vector(1.0, 1.0)
