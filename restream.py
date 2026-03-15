import subprocess
import time

YOUTUBE_URL = "https://youtu.be/vi6bpnKvVDg"
FACEBOOK_STREAM = "FB-763366903520984-0-Ab5K-DGJcARNcmOO0kiz_VPv"

def get_stream():
    url = subprocess.check_output(
        ["yt-dlp", "-f", "best", "-g", YOUTUBE_URL]
    ).decode().strip()
    return url

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

    print("Restarting in 10 seconds...")
    time.sleep(10)
