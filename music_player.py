import os
from telegram import Update
from telegram.ext import ContextTypes
from downloader import download_song
from config import BOT_TOKEN
from telegram import Bot

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Music Bot! Use /play <song name/url> to play a song.")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song_query = ' '.join(context.args)
    if song_query:
        await update.message.reply_text(f"Searching for: {song_query}")
        download_song(song_query)  # Still sync (unless you make it async too)
        await play_song(update, song_query)
    else:
        await update.message.reply_text("Please provide a song name or URL.")

async def play_song(update: Update, song_query: str):
    file_path = os.path.join('/tmp', song_query + ".mp3")

    if os.path.exists(file_path):
        bot = Bot(token=BOT_TOKEN)
        with open(file_path, 'rb') as audio_file:
            await bot.send_audio(chat_id=update.effective_chat.id, audio=audio_file)
    else:
        await update.message.reply_text("Song not found. Please try again.")
