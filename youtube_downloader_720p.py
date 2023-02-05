from pytube import YouTube
from sys import argv
import os
from pathlib import Path


'''
        📺  Youtube Video Downloader 720p

    usage in Comand Prompt: python3 youtube_video_downloader_720p.py [link]

    It is a video downloader for YouTube created using pytube and some other libraries for downloading 720p videos in mp4 format.
    
    > Insert link in place of [link] in comand prompt.
    > It can be used to download YouTube videos of only 720p size.
    > pytube is only dependency required.
    > To install pytube -> pip install pytube
    > To Batch install videos insert all links in links list

'''

# For Batch download insert all links in string type in list below.
links = []

# Checking if link is provided
try:
    link = argv[1]
except IndexError:
    link = None

# To change download location fell free to change below
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))


# YouTube video download Function
def Youtube_Downloader(Link):

    # Checking if link exists
    if link is None:
        print("😞 No link was provided so no video downloaded.")
        return

    # youtube object
    yt = YouTube(link)

    print("Title = ", yt.title)
    print("Downloading... ⏳⌛⏳⌛")

    # Selects the 720p version for video
    yd = yt.streams.get_highest_resolution()

    # Downloads the video
    yd.download(path_to_download_folder)

    print("🙂 Completed download. Enjoy. 😎")


# Calling the Youtube_Downloader function
Youtube_Downloader(link)

# Batch downloading videos
if links != []:
    for link in links:
        Youtube_Downloader(link)