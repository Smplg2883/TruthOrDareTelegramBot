import telebot

TOKEN = 'Paste ur Token for tg bot here'

bot = telebot.TeleBot(TOKEN)

users_access = {
    #paste here users id's wich one u wana use this bot with True
}

@bot.message_handler(func=lambda message: message.chat.id not in users_access or not users_access[message.chat.id], content_types=['text'])
def unknown_user(message):
    bot.send_message(message.chat.id, "U r not in list")

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    green_item = telebot.types.KeyboardButton("truth")
    red_item = telebot.types.KeyboardButton("dare")
    rules_item = telebot.types.KeyboardButton("rules")
    markup.row(green_item, red_item)
    markup.add(rules_item)
    bot.send_message(message.chat.id, "Hi , use start button for start a game", reply_markup=markup)

@bot.message_handler(func=lambda message: users_access.get(message.chat.id) == True and message.text == "truth")
def green_button(message):
    for user_id in users_access:
        if user_id != message.chat.id:
            bot.send_message(user_id, "Truth")

@bot.message_handler(func=lambda message: users_access.get(message.chat.id) == True and message.text == "dare")
def red_button(message):
    for user_id in users_access:
        if user_id != message.chat.id:
            bot.send_message(user_id, "dare")

@bot.message_handler(func=lambda message: users_access.get(message.chat.id) == True and message.text == "rules")
def rules_button(message):
    rules_text = "RULES"
    bot.send_message(message.chat.id, rules_text)

bot.polling()



