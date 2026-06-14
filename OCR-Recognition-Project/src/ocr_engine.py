import pytesseract
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text_from_image(processed_image):
    """
        Extract OCR text and metadata
    
    """
    text = pytesseract.image_to_string(processed_image)
    data = pytesseract.image_to_data(processed_image, output_type=pytesseract.Output.DATAFRAME)

    data = data.fillna("")

    return text, data