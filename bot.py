import telebot
import os
from dotenv import load_dotenv

from handlers import register_handlers

# Loading environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
	load_dotenv(dotenv_path)


class RemBot:
	def __init__(self):
		# Reading loaded environment variables.
		BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
		if not BOT_API_TOKEN:
			raise RuntimeError("BOT_API_TOKEN is not set in the environment")

		# Creating bot object
		self.bot = telebot.TeleBot(BOT_API_TOKEN)

		register_handlers(self.bot)

	def start(self):
		self.bot.polling()