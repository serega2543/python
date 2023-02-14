#import the necessary libraries
import telebot
import sqlite3

#create a bot object
bot = telebot.TeleBot('6086645191:AAG2WzHg_1ikPqonMl6G64jRTFapSyhZo68')

#create a database connection
conn = sqlite3.connect('phone_directory.db')
c = conn.cursor()

#create a table
c.execute("CREATE TABLE IF NOT EXISTS phone_directory (name TEXT, phone_number TEXT)")

#function to add new entry
@bot.message_handler(commands=['add'])
def add(message):
    #split the message text and assign it to variables
    name, phone_number = message.text.split()[1:]
    #insert the data into the table
    c.execute("INSERT INTO phone_directory VALUES (?, ?)", (name, phone_number))
    conn.commit()
    #send a confirmation message
    bot.send_message(message.chat.id, 'Entry added successfully!')

#function to search for an entry
@bot.message_handler(commands=['search'])
def search(message):
    #get the search query
    query = message.text.split()[1]
    #fetch the matching entries from the database
    c.execute("SELECT * FROM phone_directory WHERE name=?", (query,))
    result = c.fetchone()
    #check if there are any results
    if result:
        #send the matching phone number
        bot.send_message(message.chat.id, result[1])
    else:
        #send a 'not found' message
        bot.send_message(message.chat.id, 'No entry found!')

#start the bot
bot.polling()