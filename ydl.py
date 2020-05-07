#!/usr/bin/env python3
import os
import argparse
import shutil
import glob
from pytube import YouTube


def main():
    # arg parser to accept the youtube url as an argument and assign it to the variable - url
    parser = argparse.ArgumentParser(description="download audio of youtube video from provided url.")
    parser.add_argument("url", type=str, help="a url of a youtube video")
    args = parser.parse_args()
    url = args.url

    # Download the video by calling function
    download_path = (os.getenv('HOME') + '/Music')
    title = get_vid(url, download_path)

    # Rename the downloaded audio file
    os.chdir(download_path)
    f = glob.glob(f"{title}*")
    full_title = f[0]
    name = input("What do you wish to name this audio download?")
    try:
        shutil.move(full_title, name)
    except Exception as e:
        print(e)


# Function that download the audio of the given video url and returns the videos title
def get_vid(url, download_path):
    vid = YouTube(url)
    title = vid.title

    try:
        vid.streams.get_by_itag('251').download(download_path)
        print(f"Downloaded {title} in audio format at 160 kbps")
    except AttributeError:
        try:
            vid.streams.get_by_itag('140')
            print(f"Downloaded {title} in audio format at 128 kbps")
        except AttributeError:
            print("This video doesn't have good audio quality, sorry mate.")

    return title


if __name__ == "__main__":
    main()
