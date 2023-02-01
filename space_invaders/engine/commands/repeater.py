from space_invaders.engine.interfaces.command import Command


class Repeater(Command):
    """Команда, которая повторяет команду"""

    def __init__(self, command: Command):
        self._command = command

    def execute(self) -> None:
        self._command.execute()
