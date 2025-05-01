# Telegram Music VC Bot

A lightweight Telegram Music Bot that supports `/play` command to play songs in **Voice Chats (VC)** using song name or YouTube URL. Designed to run fast on low-RAM services like **Koyeb Free Tier**.

## Features

- `/play <song name or YouTube URL>` – Instantly download and play song in VC
- Fast streaming, optimized for low resources
- Supports YouTube and direct audio links
- Designed for fast deployment (0.01s response goal)

## Deployment (Koyeb)

### 1. Fork this repo

Clone or fork the repo into your GitHub account.

### 2. Set environment variables

Create a `.env` file in the root directory:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
LOGGER_ID=your_log_channel_id
MONGO_DB_URI=your_mongodb_uri
OWNER_ID=your_telegram_user_id
STRING_SESSION=your_pyrogram_string_session
