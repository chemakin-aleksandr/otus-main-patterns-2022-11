from space_invaders.engine.interfaces import Command


class BaseRepeater(Command):
    def __init__(self, cmd: Command):
        self._cmd = cmd

    def execute(self) -> None:
        self._cmd.execute()


class Repeater(BaseRepeater):
    ...


class DoubleRepeater(BaseRepeater):
    ...
