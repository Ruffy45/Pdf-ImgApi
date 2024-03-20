import pytesseract
from PIL import Image
import os

def ocr(image_folder ):
    # Set the path to the Tesseract OCR executable
    pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
    # Set the path to the folder containing the images
    # Initialize an empty string to store concatenated text
    concatenated_text = ''
    # Loop through all files in the folder
    for filename in os.listdir(image_folder):
        # Check if the file is an image
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Open the image file
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)

            # Use pytesseract to extract text from the image
            text = pytesseract.image_to_string(image)

            # Concatenate the extracted text with previous texts
            concatenated_text += text + '\n\n'

    return(concatenated_text)

    # Save the concatenated text to a single file
    output_text_file = os.path.join(image_folder, 'concatenated_text.txt')
    with open(output_text_file, 'w', encoding='utf-8') as f:
        f.write(concatenated_text)

    print(f'Concatenated text saved to {output_text_file}')
