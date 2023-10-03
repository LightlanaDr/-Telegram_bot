import telebot
from telebot import types
import logging
from datetime import datetime as dt


token = '5976128620:AAGzD8qpLmQ6s6nLh8IxRH3Aqh0Cj5d3m7g'
bot = telebot.TeleBot(token)

logging.basicConfig(level=logging.INFO)

value = ''
old_value = ''


keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton('complex', callback_data='complex'),
                telebot.types.InlineKeyboardButton('C', callback_data='C'),
                telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(   telebot.types.InlineKeyboardButton('', callback_data='no'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data=','),
                telebot.types.InlineKeyboardButton('=', callback_data='='))


@bot.message_handler(commands=['start', 'calculater'])
def start_message(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    logging.info(f'{user_id}{user_name}')
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass

    elif data == 'complex':
        data = complex(input(query.data))
        if ()
        
    elif data == 'C':
        value = '0'
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]

    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка!'

    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value != ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id = query.message.message_id, text = '0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id = query.message.message_id, text=value, reply_markup=keyboard)
            old_value = value

    old_value = value
    if value == 'Ошибка!': value =''

    time = dt.now().strftime('%H:%M')
    logging.info(f'{time} - {value}{data}')



bot.polling(non_stop=False, interval=0)
