from commands import Command


@Command(pass_args=True)
def upper(bot, update, args):
    'Upper all arguments'
    bot.sendMessage(chat_id=update.message.chat_id, text=''.join(args).upper())
