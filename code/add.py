import helper
import logging
from telebot import types, telebot
from datetime import datetime
from jproperties import Properties
import requests
import os


option = {}

configs = Properties()

with open('user.properties', 'rb') as read_prop:
    configs.load(read_prop)

api_token = str(configs.get('api_token').data)

bot = telebot.TeleBot(api_token)


if not os.path.exists("receipts"):
    os.makedirs("receipts")


def run(message, bot):
    helper.read_json()
    chat_id = message.chat.id
    option.pop(chat_id, None)  # remove temp choice
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    for c in helper.getSpendCategories():
        markup.add(c)
    msg = bot.reply_to(message, 'Select Category', reply_markup=markup)
    bot.register_next_step_handler(msg, post_category_selection, bot)


@bot.message_handler(content_types=['photo'])
def handle_uploaded_receipt(message, bot):
    try:
        chat_id = message.chat.id
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_url = 'https://api.telegram.org/file/bot{}/{}'.format(
            api_token, file_info.file_path)

        # store image
        file_extension = file_info.file_path.split('.')[-1]

        receipt_file_name = os.path.join(
            "receipts", f"receipt_{chat_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{file_extension}")

        with open(receipt_file_name, 'wb') as file:
            file.write(requests.get(file_url).content)

        bot.send_message(
            chat_id, 'Receipt uploaded successfully and The expenditure is recorded!')
    except Exception as e:
        logging.exception(str(e))
        bot.send_message(chat_id, 'Error uploading receipt. ' + str(e))


def post_category_selection(message, bot):
    try:
        chat_id = message.chat.id
        selected_category = message.text
        if selected_category not in helper.getSpendCategories():
            bot.send_message(chat_id, 'Invalid',
                             reply_markup=types.ReplyKeyboardRemove())
            raise Exception(
                "Sorry I don't recognise this category \"{}\"!".format(selected_category))

        option[chat_id] = selected_category
        message = bot.send_message(
            chat_id, 'How much did you spend on {}? \n(Enter numeric values only)'.format(str(option[chat_id])))
        bot.register_next_step_handler(
            message, post_amount_input, bot, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no! ' + str(e))
        display_text = ""
        commands = helper.getCommands()
        for c in commands:  # generate help text out of the commands dictionary defined at the top
            display_text += "/" + c + ": "
            display_text += commands[c] + "\n"
        bot.send_message(chat_id, 'Please select a menu option from below:')
        bot.send_message(chat_id, display_text)


def post_amount_input(message, bot, selected_category):
    try:
        chat_id = message.chat.id
        amount_entered = message.text
        amount_value = helper.validate_entered_amount(
            amount_entered)  # validate
        if amount_value == 0:  # cannot be $0 spending
            raise Exception("Spent amount has to be a non-zero number.")

        date_of_entry = datetime.today().strftime(
            helper.getDateFormat() + ' ' + helper.getTimeFormat())
        date_str, category_str, amount_str = str(
            date_of_entry), str(option[chat_id]), str(amount_value)
        helper.write_json(add_user_record(
            chat_id, "{},{},{}".format(date_str, category_str, amount_str)))

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.row(types.KeyboardButton("Yes, upload receipt"))
        markup.row(types.KeyboardButton("No, I'm done"))
        msg = bot.send_message(
            chat_id, 'Do you want to upload a receipt image (if available)?', reply_markup=markup)
        bot.register_next_step_handler(
            msg, handle_receipt_decision, bot, amount_str, category_str, date_str, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, 'Oh no! ' + str(e))


def handle_receipt_decision(message, bot, amount_str, category_str, date_str, selected_category):
    try:
        chat_id = message.chat.id
        decision = message.text.lower()

        if decision == "yes, upload receipt":
            bot.send_message(chat_id, 'Please upload a receipt image.')
            bot.register_next_step_handler(
                message, handle_uploaded_receipt, bot)
        elif decision == "no, i'm done":
            bot.send_message(chat_id, 'The expenditure is recorded!')
            helper.display_remaining_budget(message, bot, selected_category)
        else:
            bot.send_message(
                chat_id, 'Invalid choice. Please select "Yes, upload receipt" or "No, I\'m done".')
            markup = types.ReplyKeyboardRemove()
            msg = bot.send_message(
                chat_id, 'Do you want to upload a receipt image (if available)?', reply_markup=markup)
            bot.register_next_step_handler(
                msg, handle_receipt_decision, bot, amount_str, category_str, date_str, selected_category)
    except Exception as e:

        print(f"An exception occurred: {e}")


def add_user_record(chat_id, record_to_be_added):
    user_list = helper.read_json()
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()

    user_list[str(chat_id)]['data'].append(record_to_be_added)
    return user_list
