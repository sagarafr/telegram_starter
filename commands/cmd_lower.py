from commands import Command
from main import admin_grp


@Command(pass_args=True)
@admin_grp
def lower(bot, update, args):
    bot.sendMessage(chat_id=update.message.chat_id, text=' '.join(args).lower())
