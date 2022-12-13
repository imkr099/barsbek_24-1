from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Столица России"
    answers = [
        'Санкт-Петербург',
        'Ростов',
        'Москва',
        'Тверь',
        'Казань',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Ок",
        open_period=5,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "Столица США"
    answers = [
        "Нью-Йорк",
        "Огайо",
        "Лос-Анджелес",
        "Вашингтон",
        "Сан-Андреас",
        "Сан-Франциско",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="-",
        open_period=5,
        reply_markup=markup
    )


@dp.message_handler(commands=['mem'])
async def send_image(message: types.Message):
    photo = open('mem/dcsj9pyZOV0.jpg', 'rb')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)
    await bot.send_message(chat_id=message.from_user.id, text=int(message.text) ** 2)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)