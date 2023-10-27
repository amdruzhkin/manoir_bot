import asyncio
from manoir_bot import ManoirBot

if __name__ == "__main__":
    manoir_bot = ManoirBot()
    asyncio.run(manoir_bot.run())