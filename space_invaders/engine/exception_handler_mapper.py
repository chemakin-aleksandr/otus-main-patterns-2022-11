from space_invaders.engine.interfaces import Command, ExceptionHandler


class EmptyExceptionHandler(Command):
    def execute(self) -> None:
        pass


class ExceptionHandlerMapper(ExceptionHandler):
    def __init__(self, *, default_handler: Command | None = None) -> None:
        self._map = {}  # type:dict
        self._default_handler = default_handler or EmptyExceptionHandler()  # type:Command

    def register_handler(
        self,
        *,
        handler: Command,
        command: Command | None = None,
        exception: Exception | None = None,
    ) -> None:
        """Регистрация обработчика исключения для пары команда / исключение

        Args:
            handler (Command): Команда, вызываемая для обработки исключения
            command (Command | None): Команда, при выполнении которой возникло исключение 'exception'
            exception (Exception): Исключение, возникшее при выполнении команды 'command'
        """
        self._map[(type(command), exception)] = handler
        pass

    def handle(self, command: Command, exception: Exception) -> None:
        handler = self._map.get(
            (type(command), exception),  # сначала искать полное совпадение по команде/исключению
            self._map.get(
                (type(command), None),  # затем искать совпадение по команде
                self._map.get((type(None), exception), self._default_handler),  # затем искать по исключению
            ),
        )  # type:Command
        handler.execute()
