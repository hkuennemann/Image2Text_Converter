'''
This module uses the pytesseract library to extract text from image files.
'''

import os
from PIL import Image
import pytesseract

# Path to the folder containing the image files
# For me it's on the Desktop in a folder called "ExtractText"
folder_path = os.path.expanduser("~/Desktop/ExtractText")

# Get a list of all files in the folder
file_list = sorted(os.listdir(folder_path))

# Iterate through each file in the folder
for file_name in file_list:
    if file_name.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        # Construct the full path to the image file
        image_path = os.path.join(folder_path, file_name)

        # Open the image using PIL (Pillow)
        image = Image.open(image_path)

        # Perform OCR on the image
        text = pytesseract.image_to_string(image)

        print(f"File: {file_name}")
        print(text)
        print("=" * 50)
