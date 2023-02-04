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
            handler: Команда, вызываемая для обработки исключения
            command: Команда, при выполнении которой возникло исключение 'exception'
            exception: Исключение, возникшее при выполнении команды 'command'
        """
        self._map[(type(command), exception)] = handler
        pass

    def handle(self, command: Command, exception: Exception) -> None:
        # сначала искать полное совпадение по команде/исключению
        handler = self._map.get((type(command), exception))  # type:Command
        # если не найден, искать совпадение по команде
        handler = self._map.get((type(command), None)) if handler is None else handler
        # если не найден, искать совпадение по исключению
        handler = self._map.get((type(None), exception)) if handler is None else handler
        # вернуть handler по умолчанию, если ни одно соответствие не найдено
        handler = self._default_handler if handler is None else handler

        handler.execute()
