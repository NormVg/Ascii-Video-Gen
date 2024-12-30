from PIL import Image, ImageDraw, ImageFont


def dimen_of_char(font_path, font_size, text):

    font = ImageFont.truetype(font_path, font_size)

    # Create a dummy image to draw text on
    image = Image.new("RGB", (100, 100), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    text = set(text)
    max_width = 0

    for char in text:
        bbox = draw.textbbox((0, 0), char, font=font)  # Get bounding box for the character
        char_width = bbox[2] - bbox[0]  # Right x minus left x

        max_width = max(max_width, char_width)

    return max_width

def ascii_to_image(
    ascii_art,
    font_path="/home/vishnu/.local/share/fonts/JetBrains/JetBrains-Mono-Nerd-Font-Complete.ttf",
    font_size=12,
    image_path="ascii_art.png",
):
    # Create a new image with black background
    lines = ascii_art.splitlines()
    max_line_length = max(len(line) for line in lines)
    w = dimen_of_char(font_path, font_size, ascii_art)
    
    image_width = max_line_length * w
    image_height = len(lines) * font_size
 
    image = Image.new("RGB", (image_width, image_height), "black")
    draw = ImageDraw.Draw(image)

    # Load font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Draw the ASCII art text with white color
    y_position = 0
    for line in lines:
        draw.text((0, y_position), line, font=font, fill="white")
        y_position += font_size

    # Save the image
    image.save(image_path)