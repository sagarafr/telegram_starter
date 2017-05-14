from telegram.ext import Updater
from commands import Command
from commands import Message
from configuration.basic_configuration import BasicConfiguration


class App(object):
    def __init__(self, config_file):
        self._command = Command()
        self._message = Message()
        self._config = BasicConfiguration(config_file)
        self._updater = Updater(self._config.token)

    def run(self):
        self.command.init_dispatcher(self.updater)
        self.message.init_dispatcher(self.updater)
        self.updater.start_polling()
        self.updater.idle()

    @property
    def command(self):
        return self._command

    @property
    def message(self):
        return self._message

    @property
    def config(self):
        return self._config

    @property
    def updater(self):
        return self._updater
