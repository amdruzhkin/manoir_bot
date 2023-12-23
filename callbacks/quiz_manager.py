import time
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import ATACallbackFactory
from config import MESSAGES
from models import *


class ATAManager:
    def __init__(self):
        self.questions = MESSAGES['questions']
        self.quizes = {}

    async def run(self, message: Message, user):
        current_question = 0
        self.quizes[user.tg_id] = {
                    'start_time': int(time.time()),
                    'current_question': current_question,
                    'answers': [],
                }

        await self.create_question(message, user, current_question)

    async def create_question(self, message: Message, user, qn):
        question = MESSAGES['questions'][user.language][qn]
        keyboard = InlineKeyboardBuilder()
        for i, answer in enumerate(question['answers']):
            keyboard.button(text=answer, callback_data=ATACallbackFactory(action=f'question_{i}', value=i))
        keyboard.adjust(1)

        await message.answer(f'{question["text"]}', reply_markup=keyboard.as_markup(resize_keyboard=True))