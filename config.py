from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

BOT_TOKEN = '6931858066:AAFVkDeOkeYjsyLk0tVBiONZP2N1l5EObtY'
CHANNEL_ID = -1002135088402
dp = Dispatcher(storage=MemoryStorage())
dp.callback_query.middleware(CallbackAnswerMiddleware())