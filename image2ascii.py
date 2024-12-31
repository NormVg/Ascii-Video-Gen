from ascii_magic import AsciiArt
from PIL import ImageEnhance

import re 
def remove_ansi_escape_codes(ascii_art):
    # Regular expression to match ANSI escape sequences
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[mK]')
    return ansi_escape.sub('', ascii_art)

def imageToAsciiArt(file, enhance=False,col=120):
    my_art = AsciiArt.from_image(file)
    if enhance:
        my_art.image = ImageEnhance.Brightness(my_art.image).enhance(0.2)
    return my_art.to_ascii(columns=col)

