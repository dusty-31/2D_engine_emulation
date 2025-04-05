from game.game_engine import GameEngine
from game_objects import Vector


def main():
    # Creation of the game engine
    engine = GameEngine()
    engine.initialize(800, 600, "Factory Method Demo")

    # Creation of the scene
    engine.create_scene("MainScene")

    print("\n=== Using built-in factories ===")

    # Creation of the player through the factory
    engine.create_game_object(
        'player',
        'MainPlayer',
        texture_path='assets/player.png'
    )

    # Creation of the enemy through the factory
    engine.create_game_object(
        'enemy',
        'BasicEnemy',
        texture_path='assets/enemy.png'
    )

    # Creation of a physics body through the factory
    engine.create_game_object(
        'physics_body',
        'MovingObject',
        mass=2.0,
        position=Vector(100, 150),
        velocity=Vector(5, 0)
    )

    print("\n=== Running simulation to see all created objects ===")
    engine.run()


if __name__ == "__main__":
    main()
