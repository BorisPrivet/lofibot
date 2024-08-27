from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.command import Command
import asyncio
import logging

import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher()

kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="> =", web_app=WebAppInfo(url='https://lofibot-github-io-spcp.vercel.app/'))]], resize_keyboard=True)
# kb = ReplyKeyboardMarkup(keyboard=[KeyboardButton("> =", web_app=WebAppInfo('https://lofibot-github-io-spcp.vercel.app/'))])

# btn = [InlineKeyboardButton(text="> =", web_app=WebAppInfo(url="https://lofibot-github-io-spcp.vercel.app/"))]
# kb = InlineKeyboardMarkup().add(InlineKeyboardButton(text="> =", web_app=WebAppInfo(url="https://lofibot-github-io-spcp.vercel.app/")))

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hi! I`m lofi bot", reply_markup=kb)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())