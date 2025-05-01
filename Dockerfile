# Use slim Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y ffmpeg gcc libffi-dev libssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy bot files
COPY . .

# Expose port (for Koyeb)
EXPOSE 8080

# Run the bot
CMD ["python", "bot.py"]
