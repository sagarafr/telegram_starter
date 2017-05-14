from commands import Command


@Command()
def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="help")
