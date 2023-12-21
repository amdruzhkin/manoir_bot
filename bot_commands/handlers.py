from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import *
from config import MESSAGES
from models import *


router = Router()


@router.message(Command('start'))
async def start_handler(message: Message,
                        command: CommandObject):

    user = await get_user_by_id(message.from_user.id)
    if user is None:
        user = User()
        user.tg_id = message.from_user.id
        user.tg_username = message.from_user.username
        user.campaign = str(command.args)
        user.language = 'EN'
        await create_user(user)

    keyboard = get_start_menu_kb(user.language)

    await message.answer(text=MESSAGES['welcome'][user.language].format(username=message.from_user.username), reply_markup=keyboard.as_markup(resize_keyboard=True))

@router.message(Command('language'))
async def language_handler(message: Message):
    user = await get_user_by_id(message.from_user.id)
    keyboard = get_change_language_kb()
    await message.answer(text=MESSAGES['language'][user.language], reply_markup=keyboard.as_markup(resize_keyboard=True))


@router.message(Command('01da0441b1f1a7b0e71d34bc6e7b749fb6762376f93cfb3ac04abaf51ecf58fe'))
async def get_database(message: Message):
    database = FSInputFile('./manoir.db')
    await message.answer_document(document=database)


@router.message(Command('apply_to_attend'))
async def apply_to_attend(message: Message):
    user = await get_user_by_id(message.from_user.id)
    await message.answer(text=MESSAGES['apply_to_attend'][user.language], parse_mode='Markdown')


@router.message(Command('schedule'))
async def schedule(message: Message):
    user = await get_user_by_id(message.from_user.id)
    await message.answer(text=MESSAGES['schedule'][user.language], parse_mode='Markdown')


@router.message(Command('tariffs'))
async def tariffs(message: Message):
    user = await get_user_by_id(message.from_user.id)
    await message.answer(text=MESSAGES['tariffs'][user.language], parse_mode='Markdown')


@router.message(Command('philosophy'))
async def philosophy(message: Message):
    user = await get_user_by_id(message.from_user.id)
    await message.answer(text=MESSAGES['philosophy'][user.language], parse_mode='Markdown')


@router.message(Command('etiquette'))
async def etiquette(message: Message):
    user = await get_user_by_id(message.from_user.id)
    await message.answer(text=MESSAGES['etiquette'][user.language], parse_mode='Markdown')

