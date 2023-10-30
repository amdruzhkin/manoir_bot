from aiogram import Bot, Dispatcher

from aiogram.types import BotCommand
from config import BOT_TOKEN, dp
from handlers import router



bot_commands = [
        BotCommand(command="/quiz", description="Answer the questions to choose the option that suits you"),
        BotCommand(command="/info", description="Information about events"),
        BotCommand(command="/help", description="Bot information")
    ]

class ManoirBot(Bot):
    def __init__(self):
        super().__init__(BOT_TOKEN)


    async def run(self):
        dp.include_router(router)
        await self.set_my_commands(bot_commands)
        await self.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(self, allowed_updates=dp.resolve_used_update_types())
