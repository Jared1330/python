# -*- coding: utf-8 -*-
# t.me/tetriswefdr4231wedfrt543_bot

import telebot
import pyowm

bot = telebot.TeleBot('831420068:AAGWx-iA2C6QP5qmxclIxhhom93N29d61c0')
@bot.message_handler(commands=['start'])

def start_message(message):
        res = str(" ")
        owm = pyowm.OWM('fa5d4c47bfc6e60d075e8401154fb179')
        observation = owm.weather_at_place('Kiev')
        w = observation.get_weather()
        a= str(("Вера, привет, сейчас в Дндз +" +str(round(w.get_temperature('celsius')['temp'])) + " градусов по Цельсию."))
        res = str(a)
        bot.send_message(message.chat.id,  res )
        bot.send_sticker(message.chat.id, 'CAADAgAD5gQAAjaQ6wPuj1YgnhracwI')

bot.polling()

