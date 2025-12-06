import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
BOT_TOKEN = "8384520695:AAHd0Ua8afEOI-3jMYHok_bxaOA2UG9uk_E"
bot=Bot(token=BOT_TOKEN)
dp=Dispatcher()

dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Прувет это твой бот")
async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main()) 
