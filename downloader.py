import yt_dlp
import random
import uuid
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# List of different User-Agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
]

# Function to setup headless browser
def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver

# Function to search for song using Selenium and return URL
def search_song(driver, song_query):
    search_url = f"https://www.youtube.com/results?search_query={song_query.replace(' ', '+')}"
    driver.get(search_url)
    
    # Wait for the page to load
    time.sleep(3)  # Increase sleep time if needed
    
    # Get the first video link
    video_element = driver.find_element_by_xpath('//*[@id="video-title"]')
    video_url = video_element.get_attribute('href')
    return video_url

# Function to download song using yt-dlp
def download_song(song_query):
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

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_query])  # Automatically handles ytsearch and URL both
        return temp_file_path  # Return the path to the downloaded file
    except Exception as e:
        print(f"Error downloading song: {e}")
        return None

# Main function to run the process
def main(song_query):
    driver = setup_browser()
    
    try:
        video_url = search_song(driver, song_query)  # Get the first song URL
        print(f"Video URL: {video_url}")
        
        # Now download using yt-dlp
        temp_file_path = download_song(video_url)
        
        if temp_file_path:
            print(f"Download successful! File saved at: {temp_file_path}")
        else:
            print("Failed to download the song.")
    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    song_query = "Never Gonna Give You Up"  # Change to your song name
    main(song_query)
