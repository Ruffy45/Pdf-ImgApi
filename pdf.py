import pdf2image

def pdf_to_images(pdf_path, output_folder):
    """
    Converts a PDF file to a series of images.
    
    Args:
        pdf_path (str): The path to the input PDF file.
        output_folder (str): The path to the output folder for the images.
    
    Returns:
        list: A list of file paths for the generated images.
    """
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF object
        pdf = pdf2image.convert_from_bytes(pdf_file.read())
        
        # Set the output paths for the images
        output_paths = []
        
        # Save each page as an image
        for i, page in enumerate(pdf):
            output_path = f"{output_folder}/page_{i+1}.jpg"
            page.save(output_path, 'JPEG')
            output_paths.append(output_path)
            
    return output_paths

# pdf_path = 'test.pdf'
# output_folder = 'results'

# image_paths = pdf_to_images(pdf_path, output_folder)
# print(image_paths)