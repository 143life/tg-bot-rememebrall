import asyncio

from bot import bot, dp, scheduler
from handlers.start import start_router
from handlers.menu import set_commands

async def main():
	dp.include_router(start_router)
	await bot.delete_webhook(drop_pending_updates=True)
	await set_commands(bot)
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())