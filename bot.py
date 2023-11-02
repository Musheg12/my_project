import telebot

from MY_P import deal

from My_project import generate_mat, generate_inst
bot = telebot.TeleBot('6364341541:AAGKgBXTVYPEr0d8_AT_A6OV-mkSG8Y75P0')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, какой обьект будем проектировать?')

@bot.message_handler()
def work(message):
    if message.text.lower() == 'ok':
        bot.send_message(message.chat.id, deal(generate_mat(), generate_inst()))
bot.polling(none_stop=True, interval=0)


