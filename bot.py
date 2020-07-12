import telebot

bot = telebot.TeleBot('1378406324:AAHAhYtwvdXVyEhSx_LmYK4WRIZu_mVnX8Y');
file = open('url.txt', 'r')

url = file.readline()

@bot.message_handler(commands=['start'])
def start_message(message):

    keyboard = telebot.types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = telebot.types.InlineKeyboardButton(text='Так', callback_data='yes');
    keyboard.add(key_yes);
    key_no = telebot.types.InlineKeyboardButton(text='Ні', callback_data='no');
    keyboard.add(key_no);
    bot.send_message(message.from_user.id, text='Привіт я бот Стрілець А! Ти підписаний на групу? Меню команд: /help', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'Меню команд: \n'
                                      '/offer - запропонувати статтю або відео на переклад \n'
                                      '/imod - зображення дня від НАСА')

@bot.message_handler(commands=['offer'])
def help_command(message):
    bot.send_message(message.chat.id, 'Надішли мені посилання')

@bot.message_handler(commands=['imod'])
def send_photo(message):
    bot.send_photo(message.chat.id, url)

@bot.message_handler(content_types=['text'])
def text_check(message):
    if (message.text[0] == 'h' and message.text[1] == 't'):
        link(message)
    else:
        bot.send_message(message.chat.id, 'Це не посилання')

def link(messagge):
    text = 'Привіт, тут новий матеріал на переклад: ' + str(messagge.text)
    bot.send_message(454152497, text)
    bot.send_message(messagge.chat.id, 'Дякую, надіслав автору')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Молодець)');
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Лови посилання: https://t.me/strilecA')


bot.polling(False)
