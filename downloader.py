import yt_dlp
import os
import uuid
import random

# List of different User-Agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
]

# Function to download song with User-Agent randomization
async def download_song(song_query: str):
    # Generate a unique temp file path
    safe_filename = str(uuid.uuid4())  # Safe, random filename
    temp_file_path = f"/tmp/{safe_filename}.mp3"

    # Select a random User-Agent from the list
    user_agent = random.choice(user_agents)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': temp_file_path,
        'quiet': True,
        'default_search': 'ytsearch',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Correct key
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'user-agent': user_agent,  # Set the random User-Agent
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song_query])  # Automatically handles ytsearch and URL both

    return temp_file_path
