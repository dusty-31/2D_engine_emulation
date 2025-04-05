import math


class Vector:
    """
    A class representing a 2D vector with basic operations.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self) -> 'Vector':
        mag = self.magnitude()
        if mag == 0:
            return Vector()
        return Vector(self.x / mag, self.y / mag)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
