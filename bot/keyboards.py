from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .constants import CHAT_LINK, BUTTON_TEXT


def build_join_chat_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=BUTTON_TEXT, url=CHAT_LINK)]
        ]
    )
