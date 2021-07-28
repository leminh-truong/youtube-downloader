# This script accepts a Youtube link and download 
# the Youtube video of that link

# To use this script, first enter the following command
# into Terminal
# pip install pytube

# Then navigate to folder containing this script
# Enter following command into Terminal to run
# python youtubedownload.py

# Only works with independent videos. Playlists not yet implemented
from pytube import YouTube,Stream
import sys

def complete_func():
    print("Got YouTube object complete")

def progress_func():
    print("Getting Youtube Video")

def new_progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50-done)) )
    sys.stdout.flush()

# This function downloads a youtube video via a url
def youtube_downloader(url):
    try:
        yt = YouTube(url,
                    on_progress_callback=progress_func(),
                    on_complete_callback=complete_func())
        print(yt.title)
        mp4files = yt.streams.get_highest_resolution()

        # mp4files.download() # This will download the video to the current working directory

        # Use "output_path" for specifying folder to put videos in
        mp4files.download(output_path="YoutubeVids/")
    except:
        print("Fail to get video object")

# This function turns the youtube video into object for download
def download_youtube(url):
    try:
        yt = YouTube(url,
                    on_progress_callback=progress_func(),
                    on_complete_callback=complete_func())
        return yt
    except:
        print("Fail to get video object")

# Download youtube video
if __name__ == '__main__':
    while True:
        try:
            url = input("Enter Youtube URL: ")
            youtubeObj = download_youtube(url)
            print(youtubeObj.title)
            mp4files = youtubeObj.streams.get_highest_resolution()
            print(mp4files)

            # mp4files.download() # This will download the video to the current working directory

            # Use "output_path" for specifying folder to put videos in
            mp4files.download(output_path="YoutubeVids/")
        except:
            print("Program terminated")
            sys.exit(0)