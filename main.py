from telegram.ext import Updater
from commands import Command


def main():
    command = Command()
    updater = Updater(input("Token: "))
    command.init_dispatcher(updater)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
