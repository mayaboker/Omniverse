import os , sys
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

CSV_FILE = str(sys.argv[1])

def draw_bbox_on_image(csv_file, index):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Get the image file path from the 'Image' column for the specified index
    image_path = df.at[index, 'Image']

    # Get the bounding box parameters from the specified index
    x1 = df.at[index, 'x1']
    y1 = df.at[index, 'y1']
    x2 = df.at[index, 'x2']
    y2 = df.at[index, 'y2']

    # Get the label text from the 'LABEL' column for the specified index
    label_text = "car" #df.at[index, 'LABEL']

    # Open the image using PIL
    image = Image.open(image_path)

    # Draw the bounding box on the image
    draw = ImageDraw.Draw(image)
    draw.rectangle([(x1, y1), (x2, y2)], outline='red', width=2)

    # Define font size and font path
    font_size = 14
    font_path = "/usr/share/fonts/truetype/freefont/FreeMonoBoldOblique.ttf"  # Replace with the path to your font file

    # Load the font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Font not found. Using default font.")

    # Calculate the size of the label text to position it properly
    label_width, label_height = draw.textsize(label_text, font=font)
    label_x = x2 - label_width
    label_y = y1

    # Draw the label text on the image
    draw.text((label_x, label_y), label_text, fill='red', font=font)

    # Save the new image with the bounding box and label
    folder_path, image_filename = os.path.split(image_path)
    bbox_image_filename = f"image_with_bbox_{index}.png"
    bbox_image_path = os.path.join(folder_path, bbox_image_filename)
    image.save(bbox_image_path)

    print(f"Image with bounding box and label saved to: {bbox_image_path}")

# usage
csv_file_path = CSV_FILE
for i in range(0,20):
    print(f"starting index = {i}")
    index_to_draw = i
    draw_bbox_on_image(csv_file_path, index_to_draw)
