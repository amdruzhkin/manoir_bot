from aiogram import Router
from aiogram.types import CallbackQuery
from .factories import *
from .keyboards import get_change_language_kb
from models import *
from config import MESSAGES

router = Router()
@router.callback_query(LanguageCallbackFactory.filter())
async def language(callback: CallbackQuery, callback_data: LanguageCallbackFactory):
        user = await get_user_by_id(callback.from_user.id)
        if callback_data.value == 'change':
                keyboard = get_change_language_kb()
                await callback.message.answer(text=MESSAGES['language'][user.language], reply_markup=keyboard.as_markup())
        else:
                user.language = callback_data.value
                await update_user(user)
                if user.language == 'EN':
                        await callback.message.answer(text='Language changed to English')
                elif user.language == 'RU':
                        await callback.message.answer(text='Язык изменен на Русский')

@router.callback_query(StaticTextCallbackFactory.filter())
async def static_text(callback: CallbackQuery, callback_data: StaticTextCallbackFactory):
        user = await get_user_by_id(callback.from_user.id)
        await callback.message.answer(text=MESSAGES[callback_data.value][user.language], parse_mode='Markdown')
