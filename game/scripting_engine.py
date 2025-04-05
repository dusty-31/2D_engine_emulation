from typing import Any, Dict


class ScriptingEngine:
    """
    Class for managing and executing scripts in the game engine.
    """

    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.functions: Dict[str, callable] = {}

    @staticmethod
    def execute(script: str) -> Any:
        """
        Executes a script
        """

        print(f"Executing script: {script[:50]}...")
        # In a real engine, this would involve parsing and executing the script
        # Here is just simulate execution
        return "Script executed"

    def register_function(self, name: str, func: callable) -> None:
        """
        Registers a function to be callable from scripts
        """

        self.functions[name] = func

    def set_variable(self, name: str, value: Any) -> None:
        """
        Sets a variable to be used in scripts
        """

        self.variables[name] = value

    def get_variable(self, name: str) -> Any:
        """
        Gets a variable value by name
        """
        return self.variables.get(name)
