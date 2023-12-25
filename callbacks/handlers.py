from aiogram import Router
from aiogram.types import CallbackQuery, FSInputFile
from .factories import *
from .keyboards import get_change_language_kb
from .quiz_manager import ATAManager
from models import *
from config import MESSAGES, CHANNEL_ID


router = Router()
ata = ATAManager()

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
        answer = MESSAGES[callback_data.value]
        if 'image_src' in answer.keys():
                await callback.message.answer_photo(photo=FSInputFile(f'./images/{answer["image_src"]}'), caption=answer[user.language], parse_mode='Markdown')
        elif 'video_src' in answer.keys():
                await callback.message.answer_video(video=FSInputFile(f'./images/{answer["video_src"]}'),
                                                    caption=answer[user.language], parse_mode='Markdown')
        else:
                await callback.message.answer(text=answer[user.language], parse_mode='Markdown')

@router.callback_query(ATACallbackFactory.filter())
async def callbacks_num_change_fab(callback: CallbackQuery, callback_data: ATACallbackFactory):
        user = await get_user_by_id(callback.from_user.id)
        if callback_data.action == 'run':
                await ata.run(callback.message, user)
        else:
                current_question = ata.quizes[user.tg_id]['current_question']
                question = MESSAGES['questions']['RU'][current_question]
                ata.quizes[user.tg_id]['answers'].append(question['answers'][callback_data.value])
                ata.quizes[user.tg_id]['current_question'] += 1

                if ata.quizes[user.tg_id]['current_question'] == len(ata.questions):
                        # await callback.message.answer(MESSAGES['questions']['final_message'][user.language])

                        await callback.message.answer_photo(photo=FSInputFile(f'./images/{MESSAGES["questions"]["final_message"]["image_src"]}'),
                                     caption=MESSAGES['questions']['final_message'][user.language], parse_mode='Markdown',)

                        new_lead_text = f'Новый лид! @{callback.from_user.username}\nОтветы:\n'
                        for i, answer in enumerate(ata.quizes[user.tg_id]['answers']):
                                new_lead_text += f'{i + 1}) {answer}\n'
                        print(new_lead_text)
                        await callback.bot.send_message(chat_id=CHANNEL_ID, text=new_lead_text)
                else:
                        await ata.create_question(callback.message, user, ata.quizes[user.tg_id]['current_question'])

