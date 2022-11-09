import telebot
from Config import keys, TOKEN
from Extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}!\
\nTo convert the currencies send a message in this format:\
\n <quote currency> <base currency> <ammount>.\
\n\nTo achieve the list of available currencies use /values command")


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')
        if len(values) != 3:
            raise APIException('Incorrect number of parameters.')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'User error\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'The command cannot be executed\n{e}')
    else:
        text = f'The price of {amount} {quote} in {base} is {str(float(total_base) * float(amount))}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)