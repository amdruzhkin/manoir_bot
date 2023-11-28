from aiogram.filters.callback_data import CallbackData

class LanguageCallbackFactory(CallbackData, prefix='language'):
    action: str
    value: str