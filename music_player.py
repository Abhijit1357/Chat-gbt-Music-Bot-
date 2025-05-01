import os
from telegram import Update
from telegram.ext import ContextTypes
from downloader import download_song
from config import BOT_TOKEN
from telegram import Bot
import tempfile

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Music Bot! Use /play <song name/url> to play a song.")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song_query = ' '.join(context.args)
    if song_query:
        await update.message.reply_text(f"Searching for: {song_query}")
        temp_file_path = await download_song(song_query)  # Async download
        if temp_file_path:
            await play_song(update, temp_file_path)
        else:
            await update.message.reply_text("Song not found. Please try again.")
    else:
        await update.message.reply_text("Please provide a song name or URL.")

async def play_song(update: Update, file_path: str):
    if os.path.exists(file_path):
        bot = Bot(token=BOT_TOKEN)
        with open(file_path, 'rb') as audio_file:
            await bot.send_audio(chat_id=update.effective_chat.id, audio=audio_file)
        os.remove(file_path)  # Clean up after sending the audio
    else:
        await update.message.reply_text("Song not found. Please try again.")
