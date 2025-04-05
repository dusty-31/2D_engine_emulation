from abc import ABC, abstractmethod

from game_objects import Sprite, PhysicsBody, Vector
from scene.leaf import Leaf


class GameObjectFactory(ABC):
    """
    Abstract factory for creating game objects
    """

    @abstractmethod
    def create_object(self, name: str, **kwargs) -> Leaf:
        """
        Create a game object and wrap it in a Leaf node
        """
        pass


class SpriteFactory(GameObjectFactory):
    """
    Factory for creating sprite objects
    """

    def create_object(self, name: str, **kwargs) -> Leaf:
        """
        Create a sprite object
        """

        texture_path = kwargs.get('texture_path', '')
        sprite = Sprite(name, texture_path)

        if texture_path:
            sprite.load_texture()

        return Leaf(f"{name}Leaf", sprite)


class PhysicsBodyFactory(GameObjectFactory):
    """
    Factory for creating physics body objects
    """

    def create_object(self, name: str, **kwargs) -> Leaf:
        """
        Create a physics body object
        """
        mass = kwargs.get('mass', 1.0)
        physics_body = PhysicsBody(name, mass)

        if 'position' in kwargs:
            physics_body.transform.position = kwargs['position']

        if 'velocity' in kwargs:
            physics_body.velocity = kwargs['velocity']

        return Leaf(f"{name}Leaf", physics_body)


class EnemyFactory(GameObjectFactory):
    """
    Factory for creating enemy objects (combines sprite and physics)
    """

    def create_object(self, name: str, **kwargs) -> Leaf:
        """
        Create an enemy with both visual and physics components
        """

        texture_path = kwargs.get('texture_path', 'assets/enemy.png')
        enemy = Sprite(name, texture_path)

        if texture_path:
            enemy.load_texture()
        return Leaf(f"{name}Leaf", enemy)


class PlayerFactory(GameObjectFactory):
    """
    Factory for creating player objects (combines sprite and physics)
    """

    def create_object(self, name: str, **kwargs) -> Leaf:
        """
        Create a player with both visual and physics components
        """

        texture_path = kwargs.get('texture_path', 'assets/player.png')
        player = Sprite(name, texture_path)

        if texture_path:
            player.load_texture()
        return Leaf(f"{name}Leaf", player)

