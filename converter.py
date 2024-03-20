import requests
import base64
import os

def convert_pdf_to_base64(file_path):
    with open(file_path, "rb") as file:
        encoded_pdf = base64.b64encode(file.read()).decode('utf-8')
    return encoded_pdf

def convert_base64_to_pdf(encoded_pdf_data, output_file_path):
    decoded_pdf_data = base64.b64decode(encoded_pdf_data.encode('utf-8'))
    with open(output_file_path, "wb") as file:
        file.write(decoded_pdf_data)

def save_string_to_file(string_data, file_path):
    with open(file_path, 'w') as file:
        file.write(string_data)

# Usage

# Example usage
# pdf_file_path = "test.pdf"
# output_directory = "./results"

# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)

# encoded_pdf_data = convert_pdf_to_base64(pdf_file_path)
# save_string_to_file(encoded_pdf_data, 'output.txt')
# output_file_path = os.path.join(output_directory, "restored_file.pdf")

# convert_base64_to_pdf(encoded_pdf_data, output_file_path)
# print("PDF file restored successfully.")

