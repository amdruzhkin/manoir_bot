from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Приветственное сообщение")

@router.message(Command("info"))
async def start_handler(msg: Message):
    await msg.answer("Информация об эвентах")

@router.message(Command("help"))
async def start_handler(msg: Message):
    await msg.answer("Информация боте")
