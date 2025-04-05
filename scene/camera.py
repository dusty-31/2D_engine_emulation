from game_objects.vector import Vector


class Camera:
    """
    Class representing a camera in a 2D space.
    """

    def __init__(self, position: Vector = None, zoom: float = 1.0):
        self.position = position if position else Vector()
        self.zoom = zoom
        self.viewport_width = 1980
        self.viewport_height = 1080

    def move(self, offset: Vector) -> None:
        """
        Moves the camera by a given offset.
        """
        self.position += offset

    def set_zoom(self, zoom: float) -> None:
        """
        Sets the zoom level of the camera.
        """
        if zoom > 0:
            self.zoom = zoom

    def world_to_screen(self, world_pos: Vector) -> Vector:
        """
        Converts world coordinates to screen coordinates.
        """
        # Calculate the screen position based on the camera's position and zoom level
        screen_x = (world_pos.x - self.position.x) * self.zoom + self.viewport_width / 2
        screen_y = (world_pos.y - self.position.y) * self.zoom + self.viewport_height / 2
        return Vector(screen_x, screen_y)

    def screen_to_world(self, screen_pos: Vector) -> Vector:
        """
        Converts screen coordinates to world coordinates.
        """
        world_x = (screen_pos.x - self.viewport_width / 2) / self.zoom + self.position.x
        world_y = (screen_pos.y - self.viewport_height / 2) / self.zoom + self.position.y
        return Vector(world_x, world_y)
