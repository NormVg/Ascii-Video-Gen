import re
from tqdm import tqdm 
import video2frame
import image2ascii
import ascii2image
import fames2Video
import os
from moviepy import VideoFileClip
import random
import threading
from concurrent.futures import ThreadPoolExecutor
from  time import time
from multiprocessing import Pool
# from colorAsciiImage import coloredAsciiImage
from mulitColorAscii2Image import colored_ascii_image
file = "./car1.mp4"

s = time()

# Load the original video
video = VideoFileClip(file)

# Set the FPS to 30 and write the output video
video = video.with_fps(12)

# Save the output video
file = "input_video_24fps.mp4"
video.write_videofile(file, codec="libx264")


def remove_ansi_escape_codes(ascii_art):
    # Regular expression to match ANSI escape sequences
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[mK]')
    return ansi_escape.sub('', ascii_art)


for i in os.listdir("image-2-ascii-frames"):
    os.remove("image-2-ascii-frames/"+i)

for i in os.listdir("video-2-frame-out"):
    os.remove("video-2-frame-out/"+i)


video2frame.video_to_frames(file,"video-2-frame-out")

def process_item(i):
    col = 200
    print(f"Processing: {i}")
    imageArt = image2ascii.imageToAsciiArt("./video-2-frame-out/"+i,col=col)
    imageArt = remove_ansi_escape_codes(imageArt)

    # print(imageArt)
    colored_ascii_image(imageArt,output_image_path="./image-2-ascii-frames/ascii-art-"+i.split(".")[0]+".png",sample_image="./video-2-frame-out/"+i,width=col)
    # ascii2image.ascii_to_image(imageArt,image_path="./image-2-ascii-frames/ascii-art-"+i.split(".")[0]+".png")
    print(f"Completed: {i}")
    return f"Completed: {i}"

items = os.listdir("video-2-frame-out")


def process_all_items():
    # Use ThreadPoolExecutor to manage threads
    # with ThreadPoolExecutor(max_workers=20) as executor:
    #     # Submit tasks to the executor and collect the results
    #     results = list(tqdm(executor.map(process_item, items),total=len(items)))
    with Pool(processes=2) as pool:
        results = pool.map(process_item, items)
    print("All tasks completed!")
    return results

final_results = process_all_items()
# print(final_results)


fames2Video.create_video_from_frames(file,"image-2-ascii-frames","newhajivideo.mp4")


# Load the video file
video = VideoFileClip("newhajivideo.mp4")  # Replace with your video file path

# Save the video in MP4 format

video.write_videofile(f"ascii_output_video{random.randint(1000,1000000)}.mp4", codec="libx264")


os.remove("newhajivideo.mp4")
os.remove("input_video_24fps.mp4")
e = time()

t = (e-s)
if t >60:
    print(t/60,"min")
else:print(t,"sec")