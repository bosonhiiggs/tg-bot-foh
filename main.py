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
    item2 = types.KeyboardButton('Как дела?')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Выбери одно из двух ',reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def message(message):

    if message.text == 'Рандомное число':
        bot.send_message(message.chat.id, str(random.randint(0, 100)))
    elif message.text == 'Как дела?':
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Хорошо', callback_data='good')
        item2 = types.InlineKeyboardButton('Плохо', callback_data='bad')
        markup.add(item1, item2)

        bot.send_message(message.chat.id, "Отлично, сам как?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отлично')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Грустно')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Как дела?',
                                  reply_markup=None)

            # bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='Это Тест уведомление')
    except:
        print('123')
bot.polling(none_stop = True)