import telebot
import pyowm
import pyowm.exceptions
import time as tm
from telebot import types
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
    bot.send_message(message, chat_id, parse)


@bot.message_handler(commands=['cheer_up'])
def command_start(message):
    markup_inline = telebot.types.InlineKeyboardMarkup()  # resize_keyboard=True, one_time_keyboard=False
    item_food = telebot.types.InlineKeyboardButton(text='🥪 food', callback_data='food')
    item_walk = telebot.types.InlineKeyboardButton(text='🌿 walk', callback_data='walk')
    item_fun = telebot.types.InlineKeyboardButton(text='🎉 fun', callback_data='fun')
    item_knowledge = telebot.types.InlineKeyboardButton(text='📚 knowledge', callback_data='knowledge')
    item_idk = telebot.types.InlineKeyboardButton(text='😐 idk', callback_data='idk')
    markup_inline.add(item_food, item_walk)
    markup_inline.add(item_fun, item_knowledge)
    markup_inline.add(item_idk)
    # markup_inline.row('/food', '/walk')
    # markup_inline.row('/fun', '/knowledge')
    # markup_inline.row('/idk')
    bot.send_message(message.chat.id, "✨ Choose the category that will make you happy!\n",
                     reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'food':
        bot.send_message(call.message.chat.id, "Nice choice! Bon Appetit")
    elif call.data == 'walk':
        bot.send_message(call.message.chat.id, "Prepare your feet, it will be a long road")
    elif call.data == 'fun':
        bot.send_message(call.message.chat.id, "Have a good time!")
    elif call.data == 'knowledge':
        bot.send_message(call.message.chat.id, "Today we will learn a lot")
    elif call.data == 'idk':
        bot.send_message(call.message.chat.id, "Don't give up! I will help you")
        pass


while True:
    try:
        bot.infinity_polling(True)
    except Exception:
        tm.sleep(1)
