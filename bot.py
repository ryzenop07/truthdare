from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from handlers import *  # Import your handler functions (start, join, etc.)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher  # ✅ Must define this BEFORE using dp

    # ✅ Register callback query handler for buttons
    dp.add_handler(CallbackQueryHandler(button_handler))

    # ✅ Register command handlers
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
