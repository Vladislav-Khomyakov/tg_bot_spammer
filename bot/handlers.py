from aiogram import Router, types
from aiogram.enums import ChatType

from .constants import MESSAGE_TEXT
from .keyboards import build_join_chat_keyboard

router = Router()


@router.channel_post()
async def handle_channel_post(message: types.Message) -> None:
    # Ничего не отправляем в канал. Комментарий добавим из обсуждения на автофорварде.
    if message.chat.type != ChatType.CHANNEL:
        return


@router.message()
async def handle_discussion_autoforward(message: types.Message) -> None:
    # Реагируем на автофорвард поста канала в связанную группу обсуждений
    if message.chat.type != ChatType.SUPERGROUP:
        return
    if not getattr(message, "is_automatic_forward", False):
        return

    await message.reply(
        MESSAGE_TEXT,
        reply_markup=build_join_chat_keyboard(),
        allow_sending_without_reply=True,
    )
