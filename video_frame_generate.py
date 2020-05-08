import os
import cv2
import glob
import argparse
import numpy as np
from subprocess import call


def get_youtube_videos(key_word, count):
    """
    extracts count number of videos from youtube
    based on key_word and saves in videos folder

    youtube-dl "ytsearch10:sheep swarm"
    youtube-dl ytsearch1:sheep swarm
    """
    current_directory = os.getcwd()
    video_directory = current_directory + "/videos"
    if "videos" not in os.listdir(current_directory):
        os.mkdir(video_directory)
    os.chdir(video_directory)
    command = f"youtube-dl 'ytsearch{count}:{key_word}'"
    try:
        os.system(command)
    except:
        print("file cannot be downloaded")
    os.chdir(current_directory)

def main():
    parser = argparse.ArgumentParser(
        description="TODO")
    parser.add_argument("--key-word",
                        type=str,
                        required=True)
    parser.add_argument("--count",
                        type=str,
                        required=True)
    args = parser.parse_args()
    key_word = args.key_word
    count = args.count
    get_youtube_videos(key_word, count)

if __name__ == "__main__":
    main()

