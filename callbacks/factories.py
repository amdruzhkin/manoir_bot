from aiogram.filters.callback_data import CallbackData

class LanguageCallbackFactory(CallbackData, prefix='language'):
    action: str
    value: str

class StaticTextCallbackFactory(CallbackData, prefix='static_text'):
    value: str