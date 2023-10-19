import logging
from telebot import telebot
from jproperties import Properties
from datetime import datetime
import glob

option = {}

configs = Properties()

with open('user.properties', 'rb') as read_prop:
    configs.load(read_prop)

api_token = str(configs.get('api_token').data)

bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['receipt'])
def command_receipt(message, bot):
    chat_id = message.chat.id
    bot.send_message(
        chat_id, 'Please enter the date (YYYY-MM-DD or YYYYMMDD) for which you want to retrieve receipts:')
    bot.register_next_step_handler(message, process_date_input)


def process_date_input(message):
    try:
        chat_id = message.chat.id
        user_date = message.text.strip()
        user_date = user_date.replace("-", "")

        # Checking data format of the user-input
        try:
            datetime.strptime(user_date, "%Y%m%d")
        except ValueError:
            bot.send_message(
                chat_id, 'Invalid date format. Please use YYYY-MM-DD format.')
            return

        # Search for files in the receipts folder with the dates in their names
        matching_receipts = glob.glob(
            f"receipts/*{user_date}*")

        if matching_receipts:
            try:
                for receipt_path in matching_receipts:

                    with open(receipt_path, 'rb') as receipt_file:
                        bot.send_photo(chat_id, receipt_file)
            except Exception as e:
                logging.exception(
                    "An error occurred while sending images: " + str(e))
        else:
            bot.send_message(
                chat_id, 'No receipts found for the specified date.')

    except Exception as e:
        bot.send_message(chat_id, 'An error occurred: ' + str(e))
