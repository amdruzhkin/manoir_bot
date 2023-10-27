from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from config import BOT_TOKEN
from handlers import router

bot_commands = [
        BotCommand(command="/start", description="Start bot"),
        BotCommand(command="/quiz", description="Answer the questions to choose the option that suits you"),
        BotCommand(command="/info", description="Information about events"),
        BotCommand(command="/help", description="Bot information")
    ]

class ManoirBot(Bot):
    def __init__(self):
        super().__init__(BOT_TOKEN)
        self.dp = Dispatcher(storage=MemoryStorage())


    async def run(self):
        self.dp.include_router(router)
        await self.set_my_commands(bot_commands)
        await self.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self, allowed_updates=self.dp.resolve_used_update_types())
