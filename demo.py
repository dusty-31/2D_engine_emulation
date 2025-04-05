from game.game_engine import GameEngine
from scene.leaf import Leaf
from game_objects import PhysicsBody, Sprite


def main():
    # Створення та ініціалізація ігрового двигуна
    engine = GameEngine()
    engine.initialize(800, 600, "My 2D Game")

    # Створення сцени
    scene = engine.create_scene("MainScene")

    # Створення спрайту
    player_sprite = Sprite("Player", "assets/player.png")
    player_sprite.load_texture()

    # Створення фізичного тіла
    player_physics = PhysicsBody("PlayerPhysics", 1.0)

    # Додавання об'єктів на сцену
    scene.add_object(Leaf("PlayerLeaf", player_sprite))

    # Додавання фізичного об'єкта до фізичного двигуна
    engine.physics_engine.add_physics_object(player_physics)

    # Запуск ігрового двигуна
    engine.run()


if __name__ == "__main__":
    main()
