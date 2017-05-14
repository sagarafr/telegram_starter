from telegram.ext import Updater
from commands import Command
from commands import Message


def main():
    command = Command()
    message = Message()
    updater = Updater(input("Token: "))
    command.init_dispatcher(updater)
    message.init_dispatcher(updater)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
