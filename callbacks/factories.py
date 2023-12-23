from aiogram.filters.callback_data import CallbackData

class ATACallbackFactory(CallbackData, prefix='apply_to_attend'):
    action: str
    value: int

class LanguageCallbackFactory(CallbackData, prefix='language'):
    action: str
    value: str

class StaticTextCallbackFactory(CallbackData, prefix='static_text'):
    value: str