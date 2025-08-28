from transliterate import to_cyrillic, to_latin
import telebot 



TOKEN = "8449505846:AAFayz6LH8FK3ltk76byBnye3GeN9fDePsE"
bot = telebot.TeleBot(TOKEN, parse_mode=None) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg:  to_cyrillic(msg)if msg.isascii() else to_latin(msg)
     
    bot.reply_to(message, javob)

bot.infinity_polling()

    
    
    
