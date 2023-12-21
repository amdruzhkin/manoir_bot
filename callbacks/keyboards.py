from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import *
from config import MESSAGES


def get_start_menu_kb(lang):
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text=MESSAGES['menu']['apply_to_attend'][lang],callback_data=StaticTextCallbackFactory(value='apply_to_attend'))
    keyboard.button(text=MESSAGES['menu']['schedule'][lang],callback_data=StaticTextCallbackFactory(value='schedule'))
    keyboard.button(text=MESSAGES['menu']['philosophy'][lang], callback_data=StaticTextCallbackFactory(value='philosophy'))
    keyboard.button(text=MESSAGES['menu']['etiquette'][lang], callback_data=StaticTextCallbackFactory(value='etiquette'))
    keyboard.button(text=MESSAGES['menu']['tariffs'][lang], callback_data=StaticTextCallbackFactory(value='tariffs'))
    keyboard.button(text=MESSAGES['menu']['language'][lang], callback_data=LanguageCallbackFactory(action='change_language', value='change'))
    keyboard.adjust(1)
    return keyboard

def get_change_language_kb():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='🇬🇧 English', callback_data=LanguageCallbackFactory(action='change_language', value='EN'))
    keyboard.button(text='🇷🇺 Русский', callback_data=LanguageCallbackFactory(action='change_language', value='RU'))
    keyboard.adjust(1)
    return keyboard