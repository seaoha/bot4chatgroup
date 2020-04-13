import telebot

bot=telebot.TeleBot("1121021043:AAGsSjS0IeUFRIoHKXO0pPNAfNgqbj1J1u8")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_member.first_name
    bot.send_message(message.chat.id, "Добро пожаловать, {0}!".format(user_name))

bot.polling()
