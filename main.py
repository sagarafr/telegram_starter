from telegram.ext import Updater
from commands import Command
from commands import Message
from configuration.basic_configuration import BasicConfiguration


def main():
    command = Command()
    message = Message()
    config = BasicConfiguration('./resources/configuration.ini')
    updater = Updater(config.token)
    command.init_dispatcher(updater)
    message.init_dispatcher(updater)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
