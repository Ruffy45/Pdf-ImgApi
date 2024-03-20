import base64
import os
import shutil
from flask import Flask, request, jsonify
from pdf import pdf_to_images
from ocr import ocr
from converter import convert_base64_to_pdf

app = Flask(__name__)

@app.route('/process_pdf', methods=['POST'])
def process_pdf_api():
    # Get the base64 PDF data from the request
    base64_pdf = request.json.get('base64_pdf')

    if not base64_pdf:
        return jsonify({'error': 'Base64 PDF data is required'}), 400

    try:
        # Convert base64 to PDF file
        pdf_file = "input.pdf"
        convert_base64_to_pdf(base64_pdf, pdf_file)

        # Convert PDF to images
        output_folder = "results"
        os.makedirs(output_folder, exist_ok=True)
        pdf_to_images(pdf_file, output_folder)

        # Perform OCR on the images
        extracted_text = ocr(output_folder)

        # Clean up the temporary PDF file
        os.remove(pdf_file)

        # Remove the entire results folder
        shutil.rmtree(output_folder)

        return jsonify({'text': extracted_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)