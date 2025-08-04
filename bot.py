from telegram.ext import Updater
from telegram.ext import CallbackQueryHandler
from handlers import *

from telegram.ext import CommandHandler
from config import BOT_TOKEN

def main():
    dp.add_handler(CallbackQueryHandler(button_handler))
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("newgame", new_game))
    dp.add_handler(CommandHandler("join", join))
    dp.add_handler(CommandHandler("players", show_players))
    dp.add_handler(CommandHandler("begin", begin))
    dp.add_handler(CommandHandler("truth", truth))
    dp.add_handler(CommandHandler("dare", dare))
    dp.add_handler(CommandHandler("next", next_turn))
    dp.add_handler(CommandHandler("end", end_game))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
