from ascii_magic import AsciiArt
from PIL import ImageEnhance



def imageToAsciiArt(file):
    my_art = AsciiArt.from_image(file)
    my_art.image = ImageEnhance.Brightness(my_art.image).enhance(0.2)
    return my_art.to_ascii()

