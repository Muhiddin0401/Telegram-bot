import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import CommandStart

# 🔴 BOTFATHER DAN OLINGAN TOKEN
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


# =======================
# /start komandasi
# =======================
@dp.message(CommandStart())
async def start_handler(message: Message):
    if message.chat.type == "private":
        await message.answer(
            "👋 Assalomu alaykum!\n\n"
            "🤖 Men guruhlarda foydalanuvchi "
            "kirdi / chiqdi xabarlarini avtomatik "
            "o‘chirib beruvchi botman.\n\n"
            "📌 Qanday foydalaniladi:\n"
            "1️⃣ Meni guruhga qo‘shing\n"
            "2️⃣ Admin qiling\n"
            "3️⃣ \"Delete messages\" ruxsatini bering\n\n"
            "Shundan so‘ng bot avtomatik ishlaydi ✅"
        )
    else:
        await message.answer(
            "🤖 Men bu guruhda kirdi / chiqdi "
            "xabarlarini avtomatik o‘chiraman."
        )


# =======================
# KIRDI / CHIQDI XABARLARINI O‘CHIRISH
# =======================
@dp.message()
async def delete_join_leave(message: Message):
    # Agar foydalanuvchi kirgan yoki chiqqan bo‘lsa
    if message.new_chat_members or message.left_chat_member:
        try:
            await message.delete()
        except Exception:
            pass


# =======================
# BOTNI ISHGA TUSHIRISH
# =======================
async def main():
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
