from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from aiogram.types import Message
from aiogram.utils.markdown import hlink


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Hello!\nYour ID: {message.from_user.id}\nYour name: {message.from_user.first_name}")


@router.message(Command("help"))
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


@router.message(Command("github"))
async def send_github_repo(message: Message):
    await message.answer(
        hlink("GitHub repository", "https://github.com/dimst12/aiogram3"),
        parse_mode="HTML"
    )


@router.message(F.text == "How are you?")
async def how_are_you(message: Message):
    await message.answer("Everything is fine! Thank you!:)")


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID photo: {message.photo[-1].file_id}")


@router.message(Command("charlie"))
async def charlie_photo(message: Message):
    charlie = FSInputFile("/home/dmytros/Downloads/charlie.jpg")
    await message.answer_photo(photo=charlie, caption='This is Charlie or how Daryna (the best) calls it \'жёпа, бусина, прелесть, зараза (любя)\'!')


@router.message(Command("lika"))
async def lika_photo(message: Message):
    lika = FSInputFile("/home/dmytros/Downloads/lika.jpg")
    await message.answer_photo(photo=lika, caption='This is Lika or how Daryna and Dmytro (nicheta team))) call it🔥🔥🔥 \'жёпа, сладость, прелесть\'!')


@router.message(Command("truth"))
async def daryna_description(message: Message):
    daryna = FSInputFile("/home/dmytros/Downloads/bestie.jpg")
    await message.answer_photo(photo=daryna, caption='Это самая лучшая, прекрасная, превосходная, красивая, потрясающая, идеальная Дарина (Даринка) ❤️')


@router.message(Command("sticker"))
async def sticker(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAPJaepux1DShzZDNg8_QoJj7E4GJQEAAl9bAAKnu5hLDj1K0EPQUOw7BA')


@router.message(Command("emoji"))
async def emoji(message: Message):
    await message.answer("😎")