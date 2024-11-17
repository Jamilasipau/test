import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your bot token and channel link
BOT_TOKEN = "7905858598:AAE4-ub5pYOAKQ8GTMpzHa7vJPXtV1PUQX8"
CHANNEL_LINK = "https://t.me/join_hyponet"  # Replace with your channel link

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    # Create an inline keyboard with a join channel button
    markup = InlineKeyboardMarkup()
    join_button = InlineKeyboardButton("Join Channel", url=CHANNEL_LINK)
    markup.add(join_button)

    # Send the message with the inline button
    bot.send_message(
        message.chat.id,
        "Welcome! Please join our channel for such methods :",
        reply_markup=markup
    )

# Polling to keep the bot running
bot.polling()
