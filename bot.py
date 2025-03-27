import os
import requests

from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
APPID = os.getenv('APPID')
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'Привет! Я бот для получения погоды. Напиши /weather [город]')


@bot.message_handler(commands=['weather'])
def weather(msg):
    try:
        city = ' '.join(msg.text.split()[1:])
        if not city:
            raise ValueError("Название города не указано")

        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            "q": city,
            "units": "metric",
            "lang": "ru",
            "appid": APPID
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data['cod'] != 200:
            raise Exception(data['message'])

        info = (
            f"🌤 Погода в {data['name']}:\n"
            f"Температура: {data['main']['temp']}°C\n"
            f"Ощущается как: {data['main']['feels_like']}°C\n"
            f"Влажность: {data['main']['humidity']}%\n"
            f"Ветер: {data['wind']['speed']} м/с\n"
            f"Описание: {data['weather'][0]['description'].capitalize()}"
        )
        bot.reply_to(msg, info)

    except Exception as e:
        error = f"Ошибка: {str(e)}. Попробуйте позже или проверьте название города."
        bot.reply_to(msg, error)


bot.polling(none_stop=True, interval=0)


