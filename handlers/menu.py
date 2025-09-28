from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot):
	commands = [
		BotCommand(command="start", description="Старт"),
		BotCommand(command="start_2", description="Специальные команды"),
		BotCommand(command="start_3", description="Оценить от 1 до 10")
	]

	await bot.set_my_commands(commands, BotCommandScopeDefault())
