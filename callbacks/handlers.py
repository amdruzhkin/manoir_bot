from aiogram import Router
from aiogram.types import CallbackQuery
from callbacks import LanguageCallbackFactory

router = Router()
@router.callback_query(LanguageCallbackFactory.filter())
async def callbacks_num_change_fab(callback: CallbackQuery, callback_data: LanguageCallbackFactory):
        print(callback_data.value)