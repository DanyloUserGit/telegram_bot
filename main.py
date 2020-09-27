import telebot
import datetime
import time
import requests
from datetime import date
import config
from bs4 import BeautifulSoup as Bs

st_4 = 'CAACAgIAAxkBAAIQNl8MOa5crdFuuRGnaZHVGDQVwUbrAALVAgAC8-O-C6VG9x5J9WIuGgQ'

response = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2/2020-07-18')
soup = Bs(response.content, 'html.parser')
item = soup.find('div', class_ = 'min',).get_text(strip = True)
item2 = soup.find('div', class_ = 'max').get_text(strip = True)
token = '1309511262:AAGTfaCnxkp0uRb_KKw84cEVPNXbSlT5vuI'
today =  datetime.datetime.today()
today_out = "Сьогодні, " + str(today) + "\n" + "Температура: " + " " + str(item) + " " + ", "+ str(item2) + "\n"
bot = telebot.TeleBot(token);
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт, я бот органайзер." + "\n" + "Показую погоду, час, дату." + "\n" + "Можу вести елементарну переписку," + "\n" + "відповідати на прості питання і слати стікери." + "\n" + "\n" + " Для більшої інформації пропиши команду  /help")
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "/start - початок використання\n/help - допомога\n погода - дізнатись погоду\n")
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if(message.text == 'Привіт' or message.text == 'привіт'):
        bot.send_message(message.from_user.id, 'Привіт')
    elif(message.text == 'погода' or message.text == 'Погода'):
        bot.send_message(message.from_user.id, today_out)
    elif(message.text == 'як справи?' or message.text == 'Як справи?' or message.text == 'як справи ?' or message.text == 'Як справи ?' or message.text == 'як справи' or message.text == 'Як справи'):
        bot.send_sticker(message.chat.id, st_4)

bot.polling(none_stop=True, interval=0)