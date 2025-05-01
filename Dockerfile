FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ffmpeg gcc libffi-dev libssl-dev build-essential git curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
