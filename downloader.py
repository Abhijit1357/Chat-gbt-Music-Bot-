# downloader.py
import yt_dlp

def download_song(song_query: str):
    options = {
        'format': 'bestaudio/best',  # Best audio quality
        'outtmpl': '/tmp/%(id)s.%(ext)s',  # Temporary save path for downloaded song
        'quiet': True,  # Avoid unnecessary logs
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([song_query])  # Downloads the song directly to temporary location
