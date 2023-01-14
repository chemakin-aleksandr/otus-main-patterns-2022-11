from space_invaders.engine.interfaces.command import Command


class NoopCommand(Command):
    def execute(self) -> None:
        ...


def test_command_execute():
    assert NoopCommand().execute() is None
