import telebot
import pyowm
import pyowm.exceptions
from pyowm.exceptions import api_response_error
from config import BOT_TOKEN, OWM_TOKEN
from utils.weather import get_forecast

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)
owm = pyowm.OWM(OWM_TOKEN)