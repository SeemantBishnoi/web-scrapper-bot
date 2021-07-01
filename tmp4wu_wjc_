from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from scraper import scrape_movie


bot_token = "1894457392:AAHJUn071NRcla4TzTqePZoy-YB_b4EiMSs"

keys = ["title", "rating", "duration","summary","casts","genres"]


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hi! I can help you search movies on IMDB.\nPlease enter /movie to get started")


def movie(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Please enter the name of the movie you wish to search for!")


def search_movie(update, context):
    movie_name = update.message.text
    update.message.reply_text("You searched for "+movie_name)
    print(movie_name)
    movie_info = scrape_movie(movie_name=movie_name)
    for key in keys:
        # update.message.reply_text(
        #     "The "+key+" of the movie is "+movie_info[key])
        if type(movie_info[key]) is list:
            result = "The "+key+" are"
            for stuff in movie_info[key]:
                result+=stuff+","
            update.message.reply_text(result)    
        else:
            update.message.reply_text(
                    "The "+key+" of the movie is "+movie_info[key])

    update.message.reply_text("There you go!")


def run_bot():
    updater = Updater(bot_token)
    dp = updater.dispatcher
    start_command_handler = CommandHandler('start', start)
    movie_command_handler = CommandHandler('movie', movie)
    movie_handler = MessageHandler(Filters.text, search_movie)
    dp.add_handler(start_command_handler)
    dp.add_handler(movie_command_handler)
    dp.add_handler(movie_handler)
    updater.start_polling()
    updater.idle()


run_bot()