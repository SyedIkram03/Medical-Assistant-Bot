# import telebot
# import requests

# API_KEY = "5646xxxxxxxxxx:AAH1lLxxxxxxxxxxxxxxxxxxxxxR7I66_c"
# bot = telebot.TeleBot(API_KEY)
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_photo(message.chat.id, photo=open('welcome.png', 'rb'))
#     bot.reply_to(message,  f"Hello! {message.from_user.first_name} {message.from_user.last_name}, how may I help you?, ")


# @bot.message_handler(commands=['search'])
# def search(message):
#     query = message.text
#     query = query.replace('/search ','')
#     query = query.replace(' ','+')
#     query.capitalize()
#     # url4 = f'en.wikipedia.org/wiki/{query}'
#     url4 = f'https://www.google.com/search?q={query}'
#     # https://www.google.com/search?q=
#     # page_py = wikipediaapi.Wikipedia('en').page('elephant')
#     # bot.send_message(message.chat.id,page_py.fullurl)
#     bot.send_message(message.chat.id,url4)

# bot.polling()




from telegram import *
import response as r
import os
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, RegexHandler
from telegram.ext import Updater, Filters
import telebot


API_KEY="5646xxxxxxxxxx:AAH1lLxxxxxxxxxxxxxxxxxxxxxR7966_c"
bot = telebot.TeleBot(API_KEY)


def help(update,context):
    update.message.reply_text("Hello! This is  Medi Assist Bot.")
    update.message.reply_text(" We aim to bring to you the basic medical need that might help cure you.")
    update.message.reply_text("From hospitals to treatments, our bot can work miracles in dire needs")
    update.message.reply_text("\n We hope to own a small part in your recovery journey! Thank you!")

def exit(update,context):
    update.message.reply_text("Thank you for being with us! Team Medi-Assist wishes you the best of health.")

def symptoms(update,context):
    update.message.reply_text("Please type in your symptoms.")
    update.message.reply_text("PLEASE START THE SENTENCE WITH THE WORD: 'Symptom is or Symptoms are' ")

'''
def symptom_handle(update,context):
    text = str(update.message.text).lower()
    resp = s.sym(text)
    update.message.reply_text(resp)
'''

def hospitals(update,context):
    update.message.reply_text("Please enter the city that you live in, in the following manner.")
    update.message.reply_text("Hospitals in {your city name}.\nFor eg: Hospitals in Chennai")

def feedback(update,context):
    update.message.reply_text("Please enter your feedback!")
    update.message.reply_text('https://forms.gle/gmSSd1RTBnaUtAci6')


# @bot.message_handler(commands=['BMI'])
# def BMI(message):
#     msg = message.text
#     msg = msg.replace('/BMI ','')
#     height = float(msg[1])
#     weight = float(msg[2])
#     bmi = weight / (height ** 2)
#     if bmi < 18.5:
#         stat = "underweight"
#     elif bmi < 25:
#         stat = "normal weight"
#     elif bmi < 30:
#         stat = "overweight"
#     else:
#         stat = "obese"
#     bm=f"The BMI for {height}m & {weight}kg is {bmi}, You are {stat}"
#     bot.send_message(message.chat.id,bm)
#function testing

def BMI(update,context):
    msg = update.message.text
    msg = msg.replace('/BMI ','')
    height = float(msg[1])
    weight = float(msg[2])
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        stat = "underweight"
    elif bmi < 25:
        stat = "normal weight"
    elif bmi < 30:
        stat = "overweight"
    else:
        stat = "obese"
    bm=f"The BMI for {height}m & {weight}kg is {bmi}, You are {stat}"
    bot.send_message(message.chat.id,bm)

# def BMI(message):
#     update.message.reply_text("Please enter your Height & Body Weight:")
#     update.message.reply_text("send in this format'/BMI weight(kg) height(m)' BMI=[weight(kg)/height(m)^2]")
#     height = float(update.message.text)
#     weight = float(update.message.text)
#     bmi = weight / (height ** 2)
#     if bmi < 18.5:
#             fit = "underweight"
#     elif bmi < 25:
#         fit = "normal weight"
#     elif bmi < 30:
#         fit = "overweight"
#     else:
#         fit = "obese"
#     update.message.reply_text(bmi,fit)
            


def handle_message(update,context):
    #count=0
    text = str(update.message.text).lower()
    response=r.sample(text)
    update.message.reply_text(response)

# def calculate_bmi(bot, update):
#     # Send message asking for height
#     bot.send_message(chat_id=update.message.chat_id, text="What is your height in meters?")
#     # Define a function to handle the height response
#     def height_handler(bot, update):
#         # Get the height from the user
#         height = float(update.message.text)
#         # Send message asking for weight
#         bot.send_message(chat_id=update.message.chat_id, text="What is your weight in kilograms?")
#         # Define a function to handle the weight response
#         def weight_handler(bot, update):
#             # Get the weight from the user
#             weight = float(update.message.text)
#             # Calculate the BMI
#             bmi = weight / (height ** 2)
#             # Check if the user is fit
#             if bmi < 18.5:
#                 fit = "underweight"
#             elif bmi < 25:
#                 fit = "normal weight"
#             elif bmi < 30:
#                 fit = "overweight"
#             else:
#                 fit = "obese"
#             # Send the result to the user
#             bot.send_message(chat_id=update.message.chat_id, text="Your BMI is {:.2f} and you are {}".format(bmi, fit))
#         # Add the weight_handler function as a handler for the weight message
#         weight_message_handler = MessageHandler(Filters.text, weight_handler)
#         # Add the weight_handler function as a handler for the weight message
#         bot.dispatcher.add_handler(weight_message_handler)
#     # Add the height_handler function as a handler for the height message
#     height_message_handler = MessageHandler(Filters.text, height_handler)
#     # Add the height_handler function as a handler for the height message
#     bot.dispatcher.add_handler(height_message_handler)

def error(update,context):
    print("Error")

def main():
    updater=Updater(API_KEY,use_context=True)
    dp= updater.dispatcher
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(CommandHandler("symptoms", symptoms))
    dp.add_handler(CommandHandler("hospitals", hospitals))
    dp.add_handler(CommandHandler("Feedback", feedback))
    dp.add_handler(CommandHandler("BMI", BMI))
    dp.add_error_handler(error)
    dp.add_handler(MessageHandler(Filters.text, handle_message))


    updater.start_polling()
    updater.idle()

#count = 0
main()
