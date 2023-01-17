from space_invaders.engine.interfaces import Command


class SimpleMacroCommand(Command):
    """Простая макрокоманда.

    Выполняет цепочку команд последовательно, пока цепочка не закончится,
    либо пока не возникнет исключение.

    Args:
        commands: Список команд.
    """

    def __init__(self, commands: list[Command]):
        self._commands = commands

    def execute(self) -> None:
        """Выполнить цепочку команд."""
        for command in self._commands:
            command.execute()
