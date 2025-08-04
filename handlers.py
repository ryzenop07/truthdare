from telegram.ext import CommandHandler
from game import TruthDareGame
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from prompts import get_random_truth, get_random_dare

game = TruthDareGame()

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🌀 New Game", callback_data='newgame')],
        [InlineKeyboardButton("🔍 Truth", callback_data='truth'), InlineKeyboardButton("🔥 Dare", callback_data='dare')],
        [InlineKeyboardButton("⏭️ Next", callback_data='next')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "🎉 *Welcome to Truth & Dare!* 🎯\n\n"
        "Use the buttons or commands below to play:\n"
        "• `/newgame` – Start a new game\n"
        "• `/join` – Join the game\n"
        "• `/begin` – Begin the game\n"
        "• `/end` – End the game\n",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )

def new_game(update, context):
    game.reset()
    update.message.reply_text("🌀 New Truth & Dare game created!\nPlayers, type /join to join the game!")

def join(update, context):
    username = update.effective_user.first_name
    if game.add_player(username):
        update.message.reply_text(f"✅ {username} joined the game!")
    else:
        update.message.reply_text(f"⚠️ {username} is already in the game!")

def show_players(update, context):
    if not game.players:
        update.message.reply_text("No players have joined yet.")
    else:
        players = "\n".join([f"{i+1}. {p}" for i, p in enumerate(game.players)])
        update.message.reply_text(f"🎮 Players:\n{players}")

def begin(update, context):
    if len(game.players) < 2:
        return update.message.reply_text("Need at least 2 players to start!")
    game.started = True
    current = game.get_current_player()
    update.message.reply_text(f"Game started! 🎉\nFirst turn: {current}\nUse /truth or /dare")

def truth(update, context):
    if not game.started:
        return update.message.reply_text("Start the game with /begin.")
    player = game.get_current_player()
    update.message.reply_text(f"🧠 {player}, your Truth:\n\n{get_random_truth()}")

def dare(update, context):
    if not game.started:
        return update.message.reply_text("Start the game with /begin.")
    player = game.get_current_player()
    update.message.reply_text(f"🔥 {player}, your Dare:\n\n{get_random_dare()}")

def next_turn(update, context):
    next_player = game.next_player()
    update.message.reply_text(f"🔄 Next turn: {next_player}\nUse /truth or /dare")

def end_game(update, context):
    game.reset()
    update.message.reply_text("❌ Game ended.")

def button_handler(update, context):
    query = update.callback_query
    query.answer()

    data = query.data
    user = query.from_user.first_name

    if data == 'truth':
        query.edit_message_text(f"🧠 *{user}, your Truth:* \n\n_{get_random_truth()}_", parse_mode=ParseMode.MARKDOWN)
    elif data == 'dare':
        query.edit_message_text(f"🔥 *{user}, your Dare:* \n\n_{get_random_dare()}_", parse_mode=ParseMode.MARKDOWN)
    elif data == 'next':
        next_player = game.next_player()
        query.edit_message_text(f"⏭️ It's now *{next_player}'s* turn!\nChoose one:", parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔍 Truth", callback_data='truth'), InlineKeyboardButton("🔥 Dare", callback_data='dare')]
        ]))
    elif data == 'newgame':
        game.reset()
        query.edit_message_text("🌀 New game started! Players type /join to join!", parse_mode=ParseMode.MARKDOWN)

