import ascii_magic
from PIL import Image ,ImageEnhance
import re 
def remove_ansi_escape_codes(ascii_art):
    # Regular expression to match ANSI escape sequences
    ansi_escape = re.compile(r'\x1b\[[0-9;]*[mK]')
    return ansi_escape.sub('', ascii_art)

def generate_ascii_with_colors(image_path, output_html_path, width=120):
    # Generate ASCII art using ascii_magic
    ascii_art = ascii_magic.from_image(image_path)
    # ascii_art.image = ImageEnhance.Brightness(ascii_art.image).enhance(0.1)
    ascii_str = ascii_art.to_ascii()
    ascii_str = remove_ansi_escape_codes(ascii_str)
    # Open the original image
    img = Image.open(image_path).convert("RGB")
    img = img.resize((width, int(img.height / img.width * width * 0.55)))  # Resize to match ASCII art proportions

    # Split ASCII art into rows
    ascii_rows = ascii_str.splitlines()

    # Get image pixel colors
    pixels = img.load()

    # Start building HTML content
    html_content = """
    <html>
    <head>
        <title>Colored ASCII Art</title>
        <style>
            body {
                font-family: monospace;
                white-space: pre;
                background-color: black;
                color: white;
            }
        </style>
    </head>
    <body>
    """

    # Add colored ASCII characters
    for y, row in enumerate(ascii_rows):
        for x, char in enumerate(row):
            r, g, b = pixels[x, y]
            html_content += f'<span style="color: rgb({r},{g},{b});">{char}</span>'
        html_content += "<br>"

    # End HTML content
    html_content += """
    </body>
    </html>
    """

    # Save HTML to file
    with open(output_html_path, "w") as f:
        f.write(html_content)

    print(f"HTML file created at: {output_html_path}")

# Example usage
image_path = "video-2-frame-out/frame_0000.jpg"
output_html_path = "main.html"
generate_ascii_with_colors(image_path, output_html_path, width=120)


# imageToAsciiArt("video-2-frame-out/frame_0000.jpg")

