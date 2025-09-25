def register_handlers(bot):
	@bot.message_handler(commands=['start'])
	def start_command(message):
		bot.reply_to(message, "Привет! Я твой бот. Нужна помощь в воспоминаниях?")
	
	@bot.message_handler(commands=['help'])
	def help_command(message):
		bot.reply_to(message, "Раздел помощи. Информация")