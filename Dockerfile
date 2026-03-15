FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    nodejs \
    npm

WORKDIR /app
COPY . .

RUN pip install yt-dlp

CMD ["python", "restream.py"]
