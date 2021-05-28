import telebot
from random import randint
from config import token_1
import time

bot = telebot.TeleBot(token_1)


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, f'Привет {message.chat.username}, я бот, что тебе нужно')
    print("Message send!")


# @bot.message_handler(content_types=['text'])
# def message_add(message):
#     bot.send_message(message.chat.id, f'{message.text}')  # ДЛЯ ТОГО ТОБЫ ПЕРЕОТПРАВЛЯТЬ СООБЩЕНИЕ ОТ ЛИЦА БОТА


@bot.message_handler(commands=['game'])
def game(message):
    bot.send_message(message.chat.id, f'{message.chat.username}, Я загадал число от 1 до 10, угадай его!')
    bot.send_message(message.chat.id, f'Введи число:')
    i = randint(1, 10)
    time.sleep(5)
    ans = message.text
    ans = int(ans)
    if ans == i:
        print(ans)
        if ans == i:
            bot.send_message(message.chat.id, f'{message.chat.username}, молодец ты угадал!')
        else:
            bot.send_message(message.chat.id, f'{message.chat.username}, попробуй ещё раз! Я загадал число {i}')

    else:
        bot.send_message(message.chat.id, f"Введи число, а не текст")


bot.polling(none_stop=True)
