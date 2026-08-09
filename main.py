import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("👋 Привет! Я VPN-бот. Напиши /vpn")

@dp.message(Command("vpn"))
async def vpn(message: types.Message):
    await message.answer("🔑 Твой тестовый ключ: wg://demo-key")

@dp.message(Command("admin"))
async def admin(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("✅ Ты админ!")
    else:
        await message.answer("⛔ Доступ запрещён")

async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
