from space_invaders.engine.errors.exception_handler import ExceptionHandler
from space_invaders.engine.interfaces import Command


def run_command(cmd: Command, exception_handler: ExceptionHandler) -> None:
    """Выполнить команду с обработкой исключений"""
    try:
        cmd.execute()
    except Exception as exception:
        exception_handler.handle(cmd=cmd, exc=exception)
