from PIL import Image, ImageDraw, ImageFont
import ascii_magic
import re 
def remove_ansi_escape_codes(ascii_art):
    # Regular expression to match ANSI escape sequences
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[mK]')
    return ansi_escape.sub('', ascii_art)


def width_of_char( text,font_size=10):

    font = ImageFont.truetype("/home/vishnu/.local/share/fonts/JetBrains/JetBrains-Mono-Nerd-Font-Complete.ttf", font_size)

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

def save_colored_ascii_image(image_path, output_image_path, width=100, font_size=10):
    # Generate ASCII art
    ascii_art = ascii_magic.from_image(image_path)
    ascii_str = ascii_art.to_ascii()
    ascii_str = remove_ansi_escape_codes(ascii_str)

    # Open the original image
    img = Image.open(image_path).convert("RGB")
    img = img.resize((width, int(img.height / img.width * width * 0.55)))  # Resize to match ASCII proportions

    # Split ASCII art into rows
    ascii_rows = ascii_str.splitlines()

    # Get image pixel colors
    pixels = img.load()

    # Font setup (You can change the font file to a monospace font if needed)
    try:
        font = ImageFont.truetype("/home/vishnu/.local/share/fonts/JetBrains/JetBrains-Mono-Nerd-Font-Complete.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Determine the size of the output image
    w = width_of_char( text=ascii_str,font_size=font_size)
    char_width, char_height = w,font_size
    max_line_length = max(len(line) for line in ascii_rows)
    img_width = max_line_length * w
    img_height = len(ascii_rows) * font_size
    # img_width = char_width * width
    # img_height = char_height * len(ascii_rows)

    # Create a new blank image
    output_img = Image.new("RGB", (img_width, img_height), "black")
    draw = ImageDraw.Draw(output_img)

    # Draw ASCII characters with colors onto the new image
    for y, row in enumerate(ascii_rows):
        for x, char in enumerate(row):
            r, g, b = pixels[x, y]
            draw.text((x * char_width, y * char_height), char, fill=(r, g, b), font=font)

    # Save the resulting image
    output_img.save(output_image_path)
    print(f"Colored ASCII image saved at: {output_image_path}")


def coloredAsciiImage(ascii_str, sample_image,output_image_path, width=120, font_size=12):
# Open the original image
    image_path = sample_image
    img = Image.open(image_path).convert("RGB")
    img = img.resize((width, int(img.height / img.width * width * 0.55)))  # Resize to match ASCII proportions

    # Split ASCII art into rows
    ascii_rows = ascii_str.splitlines()

    # Get image pixel colors
    pixels = img.load()

    # Font setup (You can change the font file to a monospace font if needed)
    try:
        font = ImageFont.truetype("/home/vishnu/.local/share/fonts/JetBrains/JetBrains-Mono-Nerd-Font-Complete.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Determine the size of the output image
    w = width_of_char( text=ascii_str,font_size=font_size)
    char_width, char_height = w,font_size
    max_line_length = max(len(line) for line in ascii_rows)
    img_width = max_line_length * w
    img_height = len(ascii_rows) * font_size
    # img_width = char_width * width
    # img_height = char_height * len(ascii_rows)

    # Create a new blank image
    output_img = Image.new("RGB", (img_width, img_height), "black")
    draw = ImageDraw.Draw(output_img)

    # Draw ASCII characters with colors onto the new image
    for y, row in enumerate(ascii_rows):
        print("step 1")
        for x, char in enumerate(row):
            print("step 0")
            r, g, b = pixels[x, y]
            draw.text((x * char_width, y * char_height), char, fill=(r, g, b), font=font)

    # Save the resulting image
    output_img.save(output_image_path)
    print(f"Colored ASCII image saved at: {output_image_path}")


if __name__ =="__main__":
    from time  import time

    s = time()
    # # Example usage
    image_path = "/home/vishnu/room/dev/asciiArt-video-gen/video-2-frame-out/frame_0000.jpg"  # Replace with your image path
    output_image_path = "colored_ascii_art.png"
    save_colored_ascii_image(image_path, output_image_path, width=200, font_size=12)
    e = time()
    t = (e-s)
    if t >60:
        print(t/60,"min")
    else:print(t,"sec")