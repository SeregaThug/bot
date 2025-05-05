import asyncio
import logging

from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("1")

@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer("hell")

@dp.message(F.text == 'How are u)')
async def how_are_you(message: Message):
    await message.answer('ok!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())