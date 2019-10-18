# -*- coding: utf-8 -*-

import telebot
import pyowm
from datetime import datetime

bot = telebot.TeleBot('831420068:AAGWx-iA2C6QP5qmxclIxhhom93N29d61c0')

@bot.message_handler(commands=['start'])
def start_message(message):
        res = str(" ")
        owm = pyowm.OWM('fa5d4c47bfc6e60d075e8401154fb179')
        observation = owm.weather_at_place('Kiev')
        w = observation.get_weather()
        a= str(("Today in Kyiv is " +str(round(w.get_temperature('celsius')['temp']))))
        res = str(a)
        bot.send_message(message.chat.id,  res )
        bot.send_sticker(message.chat.id, 'CAADAgAD5gQAAjaQ6wPuj1YgnhracwI')
        log(message)


def log(message):
    my_file = open("log.txt", "a")
    my_file.write("<!------!>\n")
    date = str(datetime.now())
    my_file.write(date + '\n')
    my_file.write("<!------!>\n\n")
    my_file.close()


bot.polling()
