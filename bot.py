# bot.py
from telegram.ext import Application, CommandHandler, ContextTypes
from music_player import start, play
from config import BOT_TOKEN

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))

    # Start the bot
    app.run_polling()

if __name__ == '__main__':
    main()
