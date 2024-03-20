from pdf import pdf_to_images
from ocr import ocr
from converter import convert_base64_to_pdf
import base64
import os


def process_pdf(base64_pdf):
    # Convert base64 to PDF file
    pdf_file = "input.pdf"
    convert_base64_to_pdf(base64_pdf, pdf_file)

    # Convert PDF to images
    output_folder = "results"
    os.makedirs(output_folder, exist_ok=True)
    image_paths = pdf_to_images(pdf_file, output_folder)

    # Perform OCR on the images
    ocr(output_folder)

    # Clean up the temporary PDF file
    os.remove(pdf_file)
    for image_path in image_paths:
        os.remove(image_path)


# Example usage
def read_string_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

base64_pdf = read_string_from_file('output.txt')  # Replace with your base64 PDF string
# print(base64_pdf)
process_pdf(base64_pdf)
