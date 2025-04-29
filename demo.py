from game.game_engine import GameEngine
from scene.leaf import Leaf
from game_objects import PhysicsBody, Sprite


def main():
    """
    Main function to run the game engine.
    """
    engine = GameEngine()
    engine.initialize(800, 600, "My 2D Game")
    scene = engine.create_scene("MainScene")
    player_sprite = Sprite("Player", "assets/player.png")
    player_sprite.load_texture()
    player_physics = PhysicsBody("PlayerPhysics", 1.0)
    scene.add_object(Leaf("PlayerLeaf", player_sprite))
    engine.physics_engine.add_physics_object(player_physics)
    engine.run()


if __name__ == "__main__":
    main()
