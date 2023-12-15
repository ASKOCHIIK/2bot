import telebot
from telebot import types
# телеграм ботту издоо @NavisPythonBot

bot = telebot.TeleBot('6825593973:AAHaO2DxvXxu957Mfh4a9ERJJZnQZfWEuNs')


@bot.message_handler(content_types=['text'])
def alika(lika):
    if (lika.text == "Привет"):
        bot.send_message(lika.chat.id, text="Привеет!!!)")

    elif (lika.text == "Есть вопросы❓"):
        me = types.ReplyKeyboardMarkup(resize_keyboard=True)
        li1 = types.KeyboardButton("Кто я ?")
        li2 = types.KeyboardButton("робот ли я?")
        me.add(li1, li2)
        bot.send_message(lika.chat.id, text="какие вопросы", reply_markup=me)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("Задать вопрос❓")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я помошник Менторов по Python".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. За помощью ко мне это правильное решение!)")

    elif (message.text == "Задать вопрос❓"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Кто мой создатель ?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выбирай вопрос", reply_markup=markup)

    elif (message.text == "Кто мой создатель ?"):
        bot.send_message(message.chat.id, "Мой создатель\nимя: Аскат Кулманов\nдолжность: Ментор+(Разработчик по PYTHON)\nсоц сети:\ninstagram:--> @askochiik\ntelegram: --> @askochiik")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Я могу показать 3х месячную программу по изучению (PYTHON)")
        murkup_inline = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text='Показать', callback_data='yes')
        item_no = types.InlineKeyboardButton(text='Отменить', callback_data='no')
        murkup_inline.row(item_yes, item_no)
        bot.send_message(message.chat.id, text="Показать вам список курса?", reply_markup=murkup_inline)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.data == 'yes':
                bot.send_message(call.message.chat.id, 'Выбирай из ряда свой месяц')
                markup_inline = types.InlineKeyboardMarkup()

                # Создание кнопок для каждого месяца
                month1 = types.InlineKeyboardButton('1мес', callback_data='month1')
                month2 = types.InlineKeyboardButton('2мес', callback_data='month2')
                month3 = types.InlineKeyboardButton('3мес', callback_data='month3')

                # Добавление кнопок месяцев в разметку
                markup_inline.row(month1, month2, month3)

                # Создание кнопок для каждого месяца
                buttons_month1 = [types.InlineKeyboardButton('list')]
                buttons_month1 = [types.InlineKeyboardButton('dict')]
                buttons_month1 = [types.InlineKeyboardButton('tuple')]
                buttons_month1 = [types.InlineKeyboardButton('')]
                buttons_month1 = [types.InlineKeyboardButton('list')]
                buttons_month1 = [types.InlineKeyboardButton('list')]






                buttons_month2 = [types.InlineKeyboardButton(f'Кнопка {i + 1}', callback_data=f'month2_button{i + 1}')
                                  for i in range(5)]
                buttons_month3 = [types.InlineKeyboardButton(f'Кнопка {i + 1}', callback_data=f'month3_button{i + 1}')
                                  for i in range(5)]

                # Добавление кнопок месяцев в разметку
                markup_inline.row(*buttons_month1)
                markup_inline.row(*buttons_month2)
                markup_inline.row(*buttons_month3)

                bot.send_message(call.message.chat.id, 'Список курса:', reply_markup=markup_inline)

                @bot.callback_query_handler(func=lambda call: call.data.startswith('month'))
                def handle_month_callback(call):
                    month = call.data[5:]  # Получаем номер месяца из callback-данных

                    if month == '1':
                        buttons = [types.InlineKeyboardButton(f'Кнопка {i + 1}', callback_data=f'month1_button{i + 1}')
                                   for i in range(5)]
                    elif month == '2':
                        buttons = [types.InlineKeyboardButton(f'Кнопка {i + 1}', callback_data=f'month2_button{i + 1}')
                                   for i in range(5)]
                    elif month == '3':
                        buttons = [types.InlineKeyboardButton(f'Кнопка {i + 1}', callback_data=f'month3_button{i + 1}')
                                   for i in range(5)]

                        markup_inline = types.InlineKeyboardMarkup()
                        markup_inline.row(*buttons)

                        bot.send_message(call.message.chat.id, f'Вы выбрали {month}!', reply_markup=markup_inline)

                # Отправить список курса
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, 'Хорошо, не буду показывать список курса.')



    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("Задать вопрос❓")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не отвечаю прости..\n Мой создатель будет ругать)")

    @bot.message_handler()
    def user(message):
        if message.text == 'Bektur':
            bot.send_message(message.chat.id, 'Hi Bektur')
        elif message.text == 'Pic':
            photo = open('recent:///e58b87c4da76ed7963d8c163657acbfe', 'rb')
            bot.send_photo(message.chat.id, photo)


if __name__ == '__bot__':
    while True:
        try:
            bot.polling()
        except:
            print('Чтото сломалось перезагрузка')

bot.polling(none_stop=True)
