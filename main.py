import telebot
import random
from telebot import types


bot = telebot.TeleBot('5526916550:AAEOrt7WsI7RnDVUG__e_TbckG8L6wdVLjQ')

@bot.message_handler(commands = ['start'])
def welcome(message):
    tg_st = open('tg_stickers/AnimatedSticker.tgs', 'rb',)
    bot.send_sticker(message.chat.id, tg_st)


    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Lalalala')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Выбери одно из двух ',reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def message(message):

    if message.text == 'Рандомное число':
        bot.send_message(message.chat.id, str(random.randint(0, 100)))
    elif message.text == 'Lalalala':
        bot.send_message(message.chat.id, "Отлично")
    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить')

bot.polling(none_stop = True)