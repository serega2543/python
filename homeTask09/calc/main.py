#importing necessary libraries
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

#setting up the logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='homeTask09/calc/log.txt')

#creating the bot
bot = telegram.Bot(token='6086645191:AAG2WzHg_1ikPqonMl6G64jRTFapSyhZo68')

#function to handle the /start command
def start(update, context):
    update.message.reply_text("Hi! I'm a calculator bot. Let's get started!")

#function to handle the /calculate command
def calculate(update, context):
    text1, text2 = update.message.text.split()
    if '+' in text2:
        n1, n2 = text2.split("+")
        result = int(n1) + int(n2)
    elif '-' in text2:
        n1, n2 = text2.split("-")
        result = int(n1) - int(n2)
    elif '**' in text2:
        n1, n2 = text2.split("**")
        result = int(n1) ** int(n2)
    elif '*' in text2:
        n1, n2 = text2.split("*")
        result = int(n1) * int(n2)
    elif '/' in text2:
        n1, n2 = text2.split("/")
        result = int(n1) / int(n2)
    else:
        result = "I don't understand. Try again!"
    update.message.reply_text(result)
    logging.info("Calculated %s", f"{text2} = {result}")

#setting up the Updater
updater = Updater('6086645191:AAG2WzHg_1ikPqonMl6G64jRTFapSyhZo68', use_context=True)

#adding handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('calculate', calculate))

#starting the bot
updater.start_polling()
updater.idle()