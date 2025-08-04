from telegram.ext import CommandHandler
from game import TruthDareGame
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from prompts import get_random_truth, get_random_dare

game = TruthDareGame()

def start(update, context):
    update.message.reply_text("Welcome to Truth & Dare Bot! Use /newgame to begin.")

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
