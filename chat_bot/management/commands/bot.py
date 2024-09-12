from django.core.management.base import BaseCommand
import telebot

from chat_bot.models import QueryAnswer

bot = telebot.TeleBot('6706232016:AAH7J9nSy6YtLb3EZNzZACuTVo7fbMkLKdw')

@bot.message_handler(commands=['start'])
def handle_start(message):
    request = QueryAnswer.objects.all()[0]
    bot.send_message(message.chat.id, f"Здорова, брат! Я бот. {request.query} - {request.answer}")

@bot.message_handler(commands=['Верифицироваться'])
def handle_start(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, f"Здорова, брат! Я бот. ")

class Command(BaseCommand):
    help = 'Отображает текущее время'
    
    def handle(self, *args, **kwargs):
        bot.polling(none_stop=True)
        
        