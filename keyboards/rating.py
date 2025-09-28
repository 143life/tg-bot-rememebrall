from aiogram.utils.keyboard import ReplyKeyboardBuilder

def rating_kb():
	builder = ReplyKeyboardBuilder()
	for item in [str(i) for i in range(1, 11)]:
		builder.button(text=item)
	builder.button(text='Назад')
	builder.adjust(4, 4, 2, 1)
	return builder.as_markup(resize_keyboard=True)