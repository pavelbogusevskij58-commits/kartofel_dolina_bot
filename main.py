import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Добро пожаловать в Долину Картофеля!)

Напиши /menu чтобы сделать заказ.")

@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🥔 Заказать картофель", "📞 Связаться с фермером")
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    if message.text == "🥔 Заказать картофель":
        bot.send_message(message.chat.id, "Отлично! Напишите, сколько сеток картофеля вы хотите заказать.")
    elif message.text == "📞 Связаться с фермером":
        bot.send_message(message.chat.id, "Фермер Павел: +7 923 456-78-90")
    else:
        bot.send_message(message.chat.id, "Не понял команду. Напиши /menu.")

bot.polling(none_stop=True)
