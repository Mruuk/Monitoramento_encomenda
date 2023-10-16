import telebot
import json

def send_msg(text):
    bot_token = "YOUR_TOKEN"
    bot_chatID = "YOUR_CHATID"
    bot = telebot.TeleBot(bot_token) # conecta com o bot pela chave

    mensagem = 'OlÃ¡, essa Ã© uma mensagem de exemplo!'
    bot.send_message(chat_id=bot_chatID, text=text)

    #bot.polling() # loop, mantem o bot verificando as entradas do chat