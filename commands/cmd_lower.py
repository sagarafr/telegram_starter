from commands import Command
from main import admin


@Command(pass_args=True)
@admin
def lower(bot, update, args):
    bot.sendMessage(chat_id=update.message.chat_id, text=' '.join(args).lower())
