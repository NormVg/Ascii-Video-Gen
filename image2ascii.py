from ascii_magic import AsciiArt
from PIL import ImageEnhance

file = "/home/vishnu/room/dev/asciiArt-video-gen/frames_output/frame_0003.jpg"

def imageToAsciiArt(file):
    my_art = AsciiArt.from_image(file)
    my_art.image = ImageEnhance.Brightness(my_art.image).enhance(0.2)
    return my_art.to_ascii()

