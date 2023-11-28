from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks.factories import *
from models.user import *

router = Router()
@router.message(Command('start'))
async def start_handler(message: Message,
                        command: CommandObject):

    user = User()
    user.telegram_id = message.from_user.id
    user.username = message.from_user.username
    user.campaign = str(command.args)
    user.language = 'EN'
    await create_user(user)
    await message.answer(f'Hello, {user.username }')

@router.message(Command('language'))
async def start_handler(message: Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Русский', callback_data=LanguageCallbackFactory(action='change_language', value='RU'))
    keyboard.button(text='English', callback_data=LanguageCallbackFactory(action='change_language', value='EN'))
    keyboard.button(text='Deutsch', callback_data=LanguageCallbackFactory(action='change_language', value='DE'))
    await message.answer(text='Choose your language', reply_markup=keyboard.as_markup(resize_keyboard=True))