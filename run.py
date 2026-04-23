import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from aiogram.types import Message
from aiogram.utils.markdown import hlink
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Hello!\nYour ID: {message.from_user.id}\nYour name: {message.from_user.first_name}")


@dp.message(Command("help"))
async def get_help(message: Message):
    text = """
Current available commands:

/start — start bot
/help — list commands
/charlie — photo of Charlie
/lika — photo of Lika
/truth — Daryna
/sticker — send sticker
/emoji — test emoji
"""
    await message.answer(text)


@dp.message(Command("github"))
async def send_github_repo(message: Message):
    await message.answer(
        hlink("GitHub repository", "https://github.com/dimst12/aiogram3"),
        parse_mode="HTML"
    )


@dp.message(F.text == "How are you?")
async def how_are_you(message: Message):
    await message.answer("Everything is fine! Thank you!:)")


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")


@dp.message(Command("charlie"))
async def charlie_photo(message: Message):
    charlie = FSInputFile("/home/dmytros/Downloads/charlie.jpg")
    await message.answer_photo(photo=charlie, caption='This is Charlie or how Daryna (the best) calls it \'жёпа, бусина, прелесть, зараза (любя)\'!')


@dp.message(Command("lika"))
async def lika_photo(message: Message):
    lika = FSInputFile("/home/dmytros/Downloads/lika.jpg")
    await message.answer_photo(photo=lika, caption='This is Lika or how Daryna and Dmytro (nicheta team))) call it🔥🔥🔥 \'жёпа, сладость, прелесть\'!')


@dp.message(Command("truth"))
async def daryna_description(message: Message):
    daryna = FSInputFile("/home/dmytros/Downloads/bestie.jpg")
    await message.answer_photo(photo=daryna, caption='Это самая лучшая, прекрасная, превосходная, красивая, потрясающая, идеальная Дарина (Даринка) ❤️')


@dp.message(Command("sticker"))
async def sticker(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAPJaepux1DShzZDNg8_QoJj7E4GJQEAAl9bAAKnu5hLDj1K0EPQUOw7BA')


@dp.message(Command("emoji"))
async def emoji(message: Message):
    await message.answer("😎")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Successfully exited!")