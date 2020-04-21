import telebot
import requests

TOKEN = '1245472617:AAGaK4tAcPUsXrlk9ayTyIrZdVSrVZ8BF3M'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command1(message):
    bot.send_message(message.from_user.id, text='🌠Вы обратились в техподдержку нашего сайта.\n\n'
                                                '\😯🌠Выберите команду /support и напишите вашупроблему или предложение по поводу '
                                                'сайта.\n\nВаши сообщения будут рассмотрены в течении 24 часов.\n\n'
                                                '\💵🕐\По поводы рекламы пишите на почту wholookcompany@gmail.com')

@bot.message_handler(commands=['support'])
def command1(message):
    bot.send_message(message.from_user.id, text='✍🖍😯Как правильно заполнить ваше соообщение?\n\n'
                                                '1. Напишите ваш ник в инстаграме\n'
                                                '2. Напишите вашу проблему или ваше предложение\n\n'
                                                'Ваши сообщения будут рассмотрены в течении 24 часов.')

@bot.message_handler(func=lambda message: True)
def minecraft(message):
    bot.send_message(707614495, 'Имя: {0} {1}\n'
          'Его ID: {2}\n'
          'Текст: {3}'.format(message.from_user.first_name,
                              message.from_user.last_name,
                              str(message.from_user.id),
                              message.text))

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)