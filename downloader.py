import yt_dlp
import tempfile
import os

async def download_song(song_query: str):
    # Use yt-dlp to search and download the song asynchronously
    ydl_opts = {
        'format': 'bestaudio/best',  # Best audio quality
        'postprocessors': [{
            'key': 'FFmpegAudioConvertor',
            'preferredcodec': 'mp3',  # Convert to MP3 format
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    # Ensure the query is a search query if not a valid URL
    if not song_query.startswith("ytsearch:"):
        song_query = f"ytsearch:{song_query}"

    # Using a temporary file to store the downloaded song
    temp_file_path = os.path.join('/tmp', f'{song_query}.mp3')
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(song_query, download=True)
        video_url = info_dict.get("url", None)
        if video_url:
            ydl.download([song_query])

    return temp_file_path
