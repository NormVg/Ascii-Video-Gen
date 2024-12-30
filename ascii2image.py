from PIL import Image, ImageDraw, ImageFont

def ascii_to_image(ascii_art, font_path="/home/vishnu/.local/share/fonts/JetBrains/JetBrains-Mono-Nerd-Font-Complete.ttf", font_size=12, image_path="ascii_art.png"):
       # Create a new image with black background
    lines = ascii_art.splitlines()
    max_line_length = max(len(line) for line in lines)
    image_width = max_line_length * font_size
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

