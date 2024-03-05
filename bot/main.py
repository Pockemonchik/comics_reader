import logging
import sys
import asyncio
import os
from re import Match
from aiogram import Bot, Dispatcher,  types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import settings
from aiogram import F



dp = Dispatcher()


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
"""

ID_REGEX = r'\d{17}$'

@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    kb = [
        [types.KeyboardButton(text="/help")],
        [types.KeyboardButton(text="/description")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Что будем делать?")
    await message.answer(f"Hello, {(message.from_user.full_name)}", reply_markup=keyboard)


@dp.message(Command('help'))
async def help_handler(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode="HTML")
    # await message.delete()



@dp.message(Command("description"))
async def description_handler(message: Message) -> None:
    text = markdown.text(
        markdown.markdown_decoration.quote(
            "Бот предназначен чтения манги\n"),
    )

    await message.answer(text=text,
                         #  parse_mode=None,
                         parse_mode=ParseMode.MARKDOWN_V2,
                         )


@dp.message(F.text.regexp(ID_REGEX).as_("digits"))
async def id_handler(message: types.Message, digits: Match[str]):
    """Привязка steam id к ползователю"""
    print("found id")
    await message.answer(text=message.text,
                         parse_mode="HTML")
    # await message.delete()

@dp.message()
async def not_hadle__handler(message: types.Message):
    """если не отловлено"""
    await message.answer(text=message.text,
                         parse_mode="HTML")
    # await message.delete()

async def main() -> None:
    bot = Bot(
        token=os.environ.get("BOT_TOKEN", "6858161506:AAHGav0STjNJFDl6vqXe8oY9IZowHSwtIL8"),
        # token=settings.bot_token,
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
