import json
import time
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import dp, CHANNEL_ID

class QuizManager:
    def __init__(self):
        self.questions: dict = self.__load_questions()
        self.quizes = {}

    def __load_questions(self):
        with open('questions.json') as file:
            return json.load(file)

    async def run(self, msg: Message):
        user_id = msg.from_user.id
        start_time = int(time.time())
        current_question = 0
        self.quizes[user_id] = {
                    'start_time': start_time,
                    'current_question': current_question,
                    'answers': [],
                }

        await self.create_question(msg, current_question)

    async def create_question(self, msg, question_num):
        question = list(self.questions.keys())[question_num]
        question_text = self.questions[question]['text']

        message = f'{question}\n\n{question_text}\n\n'

        builder = InlineKeyboardBuilder()
        for i, answer in enumerate(self.questions[question]['answers']):
            message += f'{i+1}) {answer}\n'
            builder.button(text=str(i+1), callback_data=QuizCallbackFactory(action=question, value=i+1))
        builder.adjust(4)

        await msg.answer(f'{message}', reply_markup=builder.as_markup(resize_keyboard=True))



quiz_manager = QuizManager()

class QuizCallbackFactory(CallbackData, prefix="quiz"):
    action: str
    value: int

@dp.callback_query(QuizCallbackFactory.filter())
async def callbacks_num_change_fab(callback: CallbackQuery, callback_data: QuizCallbackFactory):
        user_id = callback.from_user.id
        quiz_manager.quizes[user_id]['answers'].append(callback_data.value)
        quiz_manager.quizes[user_id]['current_question'] += 1
        current_question = quiz_manager.quizes[user_id]['current_question']
        if callback_data.action == list(quiz_manager.questions.keys())[-1]:
            print()
            await callback.message.answer('Thank you for completing the survey! Manager will contact you soon.')
            new_lead_text = f'New lead! @{callback.from_user.username}\n\nLead asnwers:\n'
            for i, answer in enumerate(quiz_manager.quizes[user_id]['answers']):
                new_lead_text += f'Question {i+1}) {answer}\n'
            await callback.bot.send_message(chat_id=CHANNEL_ID, text=new_lead_text)
        else:
            await quiz_manager.create_question(callback.message, current_question)


