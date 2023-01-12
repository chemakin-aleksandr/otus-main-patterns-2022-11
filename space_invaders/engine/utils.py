from space_invaders.engine.interfaces import Command, ExceptionHandler


def safely_run_command(command: Command, exception_handler: ExceptionHandler) -> None:
    """Выполнить команду с обработкой исключений.

    Args:
        command: Команда.
        exception_handler: Обработчик исключений.
    """
    try:
        command.execute()
    except Exception as exception:
        exception_handler.handle(command=command, exception=exception)
