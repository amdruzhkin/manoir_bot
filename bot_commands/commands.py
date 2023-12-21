from aiogram.types import BotCommand

commands = [
    BotCommand(command='/start', description='Main menu'),
    BotCommand(command='/language', description='Change language'),
    BotCommand(command='/apply_to_attend', description='Apply to attend'),
    BotCommand(command='/schedule', description='Schedule'),
    BotCommand(command='/tariffs', description='Tariffs'),
    BotCommand(command='/philosophy', description='Philosophy'),
    BotCommand(command='/etiquette', description='Etiquette'),
]