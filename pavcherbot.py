from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
					  )

def greet_user (bot, update):
	text = 'Vizvan /start'
	logging.info(text)
	update.message.reply_text(text)

def talk_to_me(bot, update):
	user_text = update.message.text
	print(update.message)
	update.massage.reply_text(user_text)

def main():
	pavcherbot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

	logging.info ('bot startuet')

	dp = pavcherbot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	pavcherbot.start_polling()
	pavcherbot.idle()

main()