from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

PROXY = PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

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
	pavcherbot = Updater("953921273:AAEirj7_vQEBQpBcxrqid_TrSc_YTnG1GI0", request_kwargs=PROXY)

	logging.info ('bot startuet')

	dp = pavcherbot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	pavcherbot.start_polling()
	pavcherbot.idle()

main()