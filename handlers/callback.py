from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp

@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "Где проходит чемпионат мира по футболу в 2022г?"
    answers = [
        "Венгрия",
        "Испания",
        "США",
        "Катар",
        "Франция",
        "Иран",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Воллейбол не смотрим да",
        open_period=5,
        reply_markup=markup
    )

@dp.callback_query_handler(text="button_call_2")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 3", callback_data="button_call_3")
    markup.add(button_call_1)

    question = "Сколько будет 3+3?"
    answers = [
        "4",
        "5",
        "8",
        "6",
        "9",
        "11",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Неправильно",
        open_period=5,
        reply_markup=markup
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_2")
    dp.register_callback_query_handler(quiz_3, text="button_call_3")