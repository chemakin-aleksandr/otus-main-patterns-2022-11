from space_invaders.engine.interfaces.command import Command


class Repeater(Command):
    """Команда, которая повторяет команду"""

    def __init__(self, cmd: Command):
        self._cmd = cmd

    def execute(self) -> None:
        self._cmd.execute()
