import telebot
API_KEY = "5099142440:AAGEVP7sxDYUGBZF7Pzq7tQ0KQJarIbClAE"
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message,"Poi Valla vazhakkum Thadam idadda")


bot.polling()
