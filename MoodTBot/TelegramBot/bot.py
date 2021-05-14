import telebot
import pyowm
import pyowm.exceptions
import time as tm
from pyowm.exceptions import api_response_error
from config import BOT_TOKEN, OWM_TOKEN
from weather import get_forecast
from traffic import parse

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
owm = pyowm.OWM(OWM_TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message):
    start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    start_markup.row('/start', '/help', '/hide')
    start_markup.row('/cheer_up')
    start_markup.row('/weather', '/traffic', '/add_list')
    bot.send_message(message.chat.id, "👾 The bot has started!\n⚙ Enter /help to see bot's function's")
    bot.send_message(message.from_user.id, "⌨️ The Keyboard is added!\n⌨️ /hide To remove kb ",
                     reply_markup=start_markup)


@bot.message_handler(commands=['hide'])
def command_hide(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "⌨💤...", reply_markup=hide_markup)


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, "👾 /start - display the keyboard\n"
                                      "🌈 /cheer_up - list of places by category\n"
                                      "📝 /add_list - you can create your own list with the places you like\n"
                                      "☁ /weather - current forecast\n"
                                      "🚦 /traffic - current traffic jam in Tomsk\n")


@bot.message_handler(commands=['weather'])
def command_weather(message):
    sent = bot.send_message(message.chat.id, "🗺 Enter the City or Country\n🔍 In such format:  Toronto  or  japan")
    bot.register_next_step_handler(sent, send_forecast)


def send_forecast(message):
    try:
        get_forecast(message.text)
    except pyowm.exceptions.api_response_error.NotFoundError:
        bot.send_message(message.chat.id, "❌  Wrong place, check mistakes and try again!")
    forecast = get_forecast(message.text)
    bot.send_message(message.chat.id, forecast)


@bot.message_handler(commands=['traffic'])
def command_weather(message):
    bot.send_message(message, chat_id, parse())



while True:
    try:
        bot.infinity_polling(True)
    except Exception:
        tm.sleep(1)
