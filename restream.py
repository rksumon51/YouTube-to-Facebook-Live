import subprocess
import time

YOUTUBE_URL = "https://www.youtube.com/watch?v=VIDEO_ID"
FACEBOOK_STREAM = "rtmps://live-api-s.facebook.com:443/rtmp/YOUR_FACEBOOK_STREAM_KEY"

def get_stream():
    return subprocess.check_output(
        ["yt-dlp", "-g", YOUTUBE_URL]
    ).decode().strip()

while True:
    try:
        stream_url = get_stream()

        command = [
            "ffmpeg",
            "-re",
            "-i", stream_url,
            "-c:v", "copy",
            "-c:a", "copy",
            "-f", "flv",
            FACEBOOK_STREAM
        ]

        subprocess.run(command)

    except Exception as e:
        print("Stream error:", e)

    print("Restarting stream in 10 seconds...")
    time.sleep(10)
