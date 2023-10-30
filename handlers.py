from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from quiz_manager import quiz_manager

router = Router()

@router.message(Command("quiz"))
async def start_handler(msg: Message):
    await quiz_manager.run(msg)

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Hello message")

@router.message(Command("info"))
async def start_handler(msg: Message):
    await msg.answer("Events information")

@router.message(Command("help"))
async def start_handler(msg: Message):
    await msg.answer("Bot information")
