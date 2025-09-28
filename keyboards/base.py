from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot import admins

# Creating keyboard "Main menu"
def base_kb(user_telegram_id: int) -> ReplyKeyboardMarkup:
	kb_list = [
		[KeyboardButton(text="О боте"), KeyboardButton(text=" Профиль")],
		[KeyboardButton(text="Заполнить анкету"), KeyboardButton(text="Каталог")]
	]
	if user_telegram_id in admins:
		kb_list.append([KeyboardButton(text=" Администрирование")])
	keyboard = ReplyKeyboardMarkup(
		keyboard=kb_list,
		resize_keyboard=True,
		one_time_keyboard=True,
		input_field_placeholder=" Воспользуетесь меню?"
	)
	return keyboard