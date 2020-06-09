# -*- coding: utf-8 -*-
import telebot
import pyowm
TOKEN = '1196490495:AAHddc1IboQ_Aer6MXP2BR92dFc6W-l8dEM'
bot = telebot.TeleBot(TOKEN)
owm=pyowm.OWM('a749e5a3bd2c466fa0be3222467da4fb', language = 'en')
@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        observation = owm.weather_at_place(message.text)
        weather = observation.get_weather()
        temp=weather.get_temperature('celsius')['temp']
        answer = str(weather.get_detailed_status()) + " "
        answer += str(temp) +  " "
        if temp<10:
            answer += 'Очень холодно, оденься потеплее'
        elif temp<17:
            answer += 'Прохладно, лучше оденься'
        else:
            answer += 'Не холодно'

        bot.send_message(message.chat.id, answer)
    except pyowm.exceptions.api_response_error.NotFoundError:
        bot.send_message(message.chat.id, 'Город не найден :(')


bot.polling(none_stop = True)

