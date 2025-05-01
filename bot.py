from telegram.ext import Application, CommandHandler
from music_player import start, play
from config import BOT_TOKEN

from flask import Flask
import threading

# Flask app for health check
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return 'Bot is running!', 200

def run_flask():
    flask_app.run(host='0.0.0.0', port=8080)

def main():
    # Start Flask in a separate thread
    threading.Thread(target=run_flask).start()

    # Start Telegram bot
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.run_polling()

if __name__ == '__main__':
    main()
