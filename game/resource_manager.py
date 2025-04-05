from typing import Dict, Any


class ResourceManager:
    """
    Class for managing game resources such as textures and sounds.
    """

    def __init__(self):
        self.textures: Dict[str, Any] = {}
        self.sounds: Dict[str, Any] = {}

    def load_texture(self, name: str, path: str) -> Any:
        """
        Loads a texture from the specified path
        """

        if name in self.textures:
            return self.textures[name]

        print(f"Loading texture: {name} from {path}")

        texture = f"Texture loaded from {path}"
        self.textures[name] = texture
        return texture

    def load_sound(self, name: str, path: str) -> Any:
        """
        Loads a sound from the specified path
        """

        if name in self.sounds:
            return self.sounds[name]

        print(f"Loading sound: {name} from {path}")

        sound = f"Sound loaded from {path}"
        self.sounds[name] = sound
        return sound

    def unload_all(self) -> None:
        """
        Unloads all loaded textures and sounds.
        """

        print(f"Unloading {len(self.textures)} textures and {len(self.sounds)} sounds")
        self.textures.clear()
        self.sounds.clear()
