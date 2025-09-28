from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType

def special_kb() -> ReplyKeyboardMarkup:
	kb_list = [
		[KeyboardButton(text="Отправить геопозицию", request_location=True)],
		[KeyboardButton(text="Поделиться номером", request_contact=True)],
		[KeyboardButton(text="Отправить викторину/опрос", request_poll=KeyboardButtonPollType())]
	]
	keyboard = ReplyKeyboardMarkup(
		keyboard=kb_list,
		resize_keyboard=True,
		one_time_keyboard=True,
		input_field_placeholder="Бебебе:"
	)

	return keyboard