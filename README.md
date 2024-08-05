# Text Extraction from Images

## Overview

This Python module utilizes the `pytesseract` library to extract text from image files. It is designed to process image files from a specified folder and output the extracted text for each image.

## Requirements

- **Python 3.x**: Ensure you have Python 3 installed on your system.
- **Libraries**: The script requires the following libraries:
  - `pytesseract`
  - `pillow` (PIL fork)

## Usage

1. **Prepare Your Image Folder**

   Place all the images from which you want to extract text in a folder. Update the `folder_path` variable in the script to point to this folder. For example, if your folder is on the Desktop and named "ExtractText", set:

   ```python
   folder_path = os.path.expanduser("~/Desktop/ExtractText")
   ```

2. **Run the Script**

   Execute the script from your terminal or command prompt:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of your Python file.

3. **Script Output**

   The script will:
   - Iterate through all image files (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`) in the specified folder.
   - Extract text from each image using `pytesseract`.
   - Print the filename and the extracted text to the console.

## Example

If your folder contains an image file named `sample_image.jpg`, the output will look something like this:

```
File: sample_image.jpg
Extracted text from the image

==================================================
```

## Troubleshooting

- Ensure that Tesseract-OCR is correctly installed and available in your system's PATH.
- Verify that the folder path is correct and that it contains image files.
- If you encounter issues, consult the [pytesseract documentation](https://pytesseract.readthedocs.io/en/latest/) or the [Tesseract-OCR documentation](https://github.com/tesseract-ocr/tesseract).
