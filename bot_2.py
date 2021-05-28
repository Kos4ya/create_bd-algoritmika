import telebot
import random
from config import token_2
from telebot import types
import constants, os, re
import requests
from bs4 import BeautifulSoup

#text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

URL = 'https://www.gismeteo.ru/weather-surgut-3994/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Accept': '*/*'
}
bot = telebot.TeleBot(token_2)


@bot.message_handler(commands=['start'])
def inline(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
    but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
    but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
    but_4 = types.InlineKeyboardButton(text="Number4", callback_data="Number4")
    key.add(but_1, but_2, but_3, but_4)
    bot.send_message(message.chat.id, "ВЫБЕРИТЕ КНОПКУ", reply_markup=key)


@bot.callback_query_handler(func=lambda c: True)
def inlin(c):
    if c.data == 'NumberOne':
        bot.send_message(c.message.chat.id, 'Это кнопка 1')
    if c.data == 'NumberTwo':
        bot.send_message(c.message.chat.id, 'Это кнопка 2')
    if c.data == 'NumberTree':
        bot.send_message(c.message.chat.id, 'Это кнопка 3')
    if c.data == 'Number4':
        bot.send_message(c.message.chat.id, 'Это кнопка 4')


@bot.message_handler(commands=['game'])
def welcome(message, where_call=None):
    sticker = open("sticker.png", "rb")
    bot.send_sticker(message.chat.id, sticker)
    if where_call is None:
        global number
        number = random.randint(1, 30)
        msg = bot.send_message(message.chat.id, 'Сможешь угадать число между 1 и 30?')
        attempt = 1
        bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))
    elif where_call == 'not_digit':
        msg = bot.send_message(message.chat.id, 'только числа')
        attempt = 1
        bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))


def random_number(message, attempt):
    if message.text.isdigit():
        n = int(message.text)
        attempt += 1
        if n < number:
            msg = bot.send_message(message.chat.id, 'мало\nещё')
            bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))
        elif n > number:
            msg = bot.send_message(message.chat.id, 'много\nещё')
            bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))
        else:
            bot.send_message(message.chat.id, f'угадал, с {attempt - 1} попытки!')
    else:
        welcome(message, where_call='not_digit')


bot.polling(none_stop=True, interval=0)
