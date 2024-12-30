import re
from tqdm import tqdm 
import video2frame
import image2ascii
import ascii2image
import fames2Video
import os
from moviepy import VideoFileClip


file = "/home/vishnu/room/dev/asciiArt-video-gen/ac75088a634c44ac390aee0c819c89d4.mp4"

# from moviepy.editor import VideoFileClip

# Load the original video
video = VideoFileClip(file)

# Set the FPS to 30 and write the output video
video = video.with_fps(24)

# Save the output video
file = "input_video_24fps.mp4"
video.write_videofile(file, codec="libx264")


def remove_ansi_escape_codes(ascii_art):
    # Regular expression to match ANSI escape sequences
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[mK]')
    return ansi_escape.sub('', ascii_art)


try:
    os.removedirs("image-2-ascii-frames")
except:pass

try:
    os.mkdir("image-2-ascii-frames")
except:pass

video2frame.video_to_frames(file,"video-2-frame-out")

for i in tqdm( os.listdir("video-2-frame-out")):
    # print(i)
    imageArt = image2ascii.imageToAsciiArt("./video-2-frame-out/"+i)
    imageArt = remove_ansi_escape_codes(imageArt)

    # print(imageArt)
   
    ascii2image.ascii_to_image(imageArt,image_path="./image-2-ascii-frames/ascii-art-"+i.split(".")[0]+".png")

fames2Video.create_video_from_frames(file,"image-2-ascii-frames","newhajivideo.mp4")


# Load the video file
video = VideoFileClip("newhajivideo.mp4")  # Replace with your video file path

# Save the video in MP4 format
video.write_videofile("ascii_output_video.mp4", codec="libx264")