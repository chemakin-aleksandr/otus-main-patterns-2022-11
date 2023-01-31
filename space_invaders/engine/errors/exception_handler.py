from queue import Queue

from space_invaders.engine.commands import Rotate
from space_invaders.engine.commands.check_fuel import CheckFuel
from space_invaders.engine.commands.log_writer import LogWriter
from space_invaders.engine.commands.move import Move
from space_invaders.engine.commands.repeater import Repeater, DoubleRepeater
from space_invaders.engine.interfaces import Command, BaseExceptionHandler


class ExceptionHandler(BaseExceptionHandler):

    def __init__(self, queue: Queue):
        self.queue = queue
        self.exc_dispatcher = {
            Move:           self.double_repeater_handler,
            Rotate:         self.log_handler,
            CheckFuel:      self.repeater_handler,
            Repeater:       self.log_handler,
            DoubleRepeater: self.repeater_handler,
            LogWriter:      self.default_handler,
        }

    def handle(self, cmd: Command, exc: Exception):
        exc_handler = self.exc_dispatcher.get(type(cmd), self.default_handler)
        exc_handler(cmd, exc)

    def default_handler(self, cmd: Command, exc: Exception):
        print(f'{cmd=} {exc=}')

    def repeater_handler(self, cmd: Command, exc: Exception):
        self.queue.put(Repeater(cmd=cmd))

    def double_repeater_handler(self, cmd: Command, exc: Exception):
        self.queue.put(DoubleRepeater(cmd=Repeater(cmd)))

    def log_handler(self, cmd: Command, exc: Exception):
        self.queue.put(LogWriter(exc=exc))
