from PIL import Image, ImageDraw, ImageFont

import numpy as np

def width_of_char(text, font_size=10):
    font = ImageFont.truetype(
        "/home/vishnu/.local/share/fonts/JetBrains/JetBrains-Mono-Nerd-Font-Complete.ttf", font_size
    )
    image = Image.new("RGB", (100, 100), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    text = set(text)
    max_width = 0
    for char in text:
        bbox = draw.textbbox((0, 0), char, font=font)
        char_width = bbox[2] - bbox[0]
        max_width = max(max_width, char_width)

    return max_width

def render_row(args):
    # print("process start")
    """Render a single row of ASCII characters."""
    y, row, colors, char_width, char_height, font = args
    row_image = Image.new("RGB", (len(row) * char_width, char_height), "black")
    draw = ImageDraw.Draw(row_image)
    for x, char in enumerate(row):
        r, g, b = colors[y][x]
        draw.text((x * char_width, 0), char, fill=(r, g, b), font=font)
    # print("process end")
    return row_image

def colored_ascii_image(ascii_str, sample_image, output_image_path, width=120, font_size=12):
    # Open the original image and resize
    img = Image.open(sample_image).convert("RGB")
    img = img.resize((width, int(img.height / img.width * width * 0.55)))  # Resize for ASCII proportions

    # Split ASCII art into rows
    ascii_rows = ascii_str.splitlines()

    # Convert image to NumPy array for fast pixel access
    img_np = np.array(img)

    # Load font
    try:
        font = ImageFont.truetype(
            "/home/vishnu/.local/share/fonts/JetBrains/JetBrains-Mono-Nerd-Font-Complete.ttf", font_size
        )
    except IOError:
        font = ImageFont.load_default()

    # Determine the size of the output image
    char_width = width_of_char(ascii_str, font_size=font_size)
    char_height = font_size
    img_width = len(ascii_rows[0]) * char_width
    img_height = len(ascii_rows) * char_height

    # Prepare arguments for multiprocessing
    args = [
        (y, row, img_np, char_width, char_height, font)
        for y, row in enumerate(ascii_rows)
    ]


    row_images = []
    for ar in args:
        row_images.append(render_row(ar))



    # Combine all row images into a single output image
    output_img = Image.new("RGB", (img_width, img_height), "black")
    for y, row_image in enumerate(row_images):
        output_img.paste(row_image, (0, y * char_height))

    # Save the final output
    output_img.save(output_image_path)
    print(f"Colored ASCII image saved at: {output_image_path}")

# Example usage:

#colored_ascii_image(ascii_art, "sample.jpg", "output_image.jpg", width=120, font_size=12)



if __name__ =="__main__":
    
    from time  import time
    import image2ascii

    image_path = "/home/vishnu/room/dev/asciiArt-video-gen/video-2-frame-out/frame_0001.jpg"  # Replace with your image path
    image2ascii.imageToAsciiArt(image_path)
    ascii_str = image2ascii.remove_ansi_escape_codes(image2ascii.imageToAsciiArt(image_path))
    s = time()
    # # Example usage
    output_image_path = "colored_ascii_art.png"
    colored_ascii_image(ascii_str, image_path, "asd_output_image.png", width=200, font_size=12)
    e = time()
    t = (e-s)
    if t >60:
        print(t/60,"min")
    else:print(t,"sec")