from pytube import YouTube
from validators import url

# Functions to be called during download process
def on_download_complete(stream, file_path) -> None:
    """Prints a message upon download completion, including file path and stream resolution (if available)."""
    print(f"Download complete! Video saved at {file_path}")
    print(f"Stream resolution: {stream.resolution}\n")

def on_progress(stream, chunk, bytes_remaining) -> None:
    """Prints download progress information as percentage and downloaded bytes."""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_complete = (bytes_downloaded / total_size) * 100

    print(f"Progress: {round(percent_complete, 2)}%, Downloaded: {bytes_downloaded} bytes out of {total_size}\n")

# Main program loop
while True:
    user_url = input("Enter a valid YouTube video URL: ")

    # Validate URL format and ensure it's a YouTube link
    if url(user_url) and ("youtu.be" in user_url or "youtube.com" in user_url):
        break
    else:
        print("Invalid URL. Please enter a valid YouTube video URL.")

# Create YouTube object with user-provided URL and callback functions
yt = YouTube(user_url, on_progress_callback=on_progress, on_complete_callback=on_download_complete)

# Select and download the stream (720p progressive in this example)
stream = yt.streams.filter(progressive=True, res="720p").first()
stream.download()

# Print additional video information
print(f"Video title: {yt.title}.")
print(f"Author: {yt.author}")
print(f"Length : {yt.length} seconds.")