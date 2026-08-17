import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# --- НАСТРОЙКИ ---
BOT_TOKEN = "ВСТАВЬ_СЮДА_ТОКЕН_ОТ_BOTFATHER"
WEBAPP_URL = "https://твойник.github.io/repo/jager_casino_demo.html"  # ссылка из шага 2

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def play_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎰 Играть",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Добро пожаловать в JAGER — демо-версия на игровой валюте.\n"
        "Реальных денег, выводов и ставок здесь нет — только фишки для теста.",
        reply_markup=play_keyboard(),
    )


@dp.message(F.text.lower() == "играть")
async def play_handler(message: Message):
    await message.answer("Жми на кнопку ниже:", reply_markup=play_keyboard())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
