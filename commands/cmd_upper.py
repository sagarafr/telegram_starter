from commands import Command


@Command(pass_args=True)
def upper(bot, update, args):
    bot.sendMessage(chat_id=update.message.chat_id, text=''.join(args).upper())
