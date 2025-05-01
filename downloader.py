import yt_dlp

def download_song(song_query):
    # Use yt-dlp to search and download the song
    ydl_opts = {
        'format': 'bestaudio/best',  # Best audio quality
        'postprocessors': [{
            'key': 'FFmpegAudioConvertor',
            'preferredcodec': 'mp3',  # Convert to MP3 format
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Perform search and download
        if not song_query.startswith("ytsearch:"):
            song_query = "ytsearch:" + song_query  # Prefix for YouTube search
        ydl.download([song_query])  # Downloads the song directly to temporary location
