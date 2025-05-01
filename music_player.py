# music_player.py
import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext
from downloader import download_song
from config import BOT_TOKEN

def play_song(update: Update, song_query: str):
    # Path to the downloaded audio file
    file_path = os.path.join('/tmp', song_query + ".mp3")

    # Check if the file exists and send it directly
    if os.path.exists(file_path):
        bot = Bot(token=BOT_TOKEN)

        # Send the audio file to the VC
        with open(file_path, 'rb') as audio_file:
            bot.send_audio(chat_id=update.message.chat_id, audio=audio_file)

    else:
        update.message.reply_text("Song not found. Please try again.")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to Music Bot! Use /play <song name/url> to play a song.")

def play(update: Update, context: CallbackContext):
    song_query = ' '.join(context.args)
    if song_query:
        update.message.reply_text(f"Searching for: {song_query}")
        download_song(song_query)  # Download the song
        play_song(update, song_query)  # Play the song immediately in VC
    else:
        update.message.reply_text("Please provide a song name or URL.")
