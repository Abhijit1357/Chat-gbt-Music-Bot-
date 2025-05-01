import yt_dlp
import os
import uuid

async def download_song(song_query: str):
    # Generate a unique temp file path
    safe_filename = str(uuid.uuid4())  # Safe, random filename
    temp_file_path = f"/tmp/{safe_filename}.mp3"

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
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song_query])  # Automatically handles ytsearch and URL both

    return temp_file_path
