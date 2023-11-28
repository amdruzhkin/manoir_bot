import asyncio
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
import callbacks
import bot_commands

bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dispatcher = Dispatcher(storage=storage)
dispatcher.callback_query.middleware(CallbackAnswerMiddleware())

async def main():
    dispatcher.include_router(router=bot_commands.router)
    dispatcher.include_router(router=callbacks.router)
    await bot.set_my_commands(bot_commands.commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
