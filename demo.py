from game.game_engine import GameEngine
from scene.leaf import Leaf
from game_objects import PhysicsBody, Sprite


def main():
    # Creation of the game engine
    engine = GameEngine()
    engine.initialize(800, 600, "My 2D Game")

    # Creation of the scene
    scene = engine.create_scene("MainScene")

    # Creation of the player sprite
    player_sprite = Sprite("Player", "assets/player.png")
    player_sprite.load_texture()

    # Creation of the player physics body
    player_physics = PhysicsBody("PlayerPhysics", 1.0)
    scene.add_object(Leaf("PlayerLeaf", player_sprite))

    # Adding the physics body to the scene
    engine.physics_engine.add_physics_object(player_physics)

    # Running the game engine
    engine.run()


if __name__ == "__main__":
    main()
