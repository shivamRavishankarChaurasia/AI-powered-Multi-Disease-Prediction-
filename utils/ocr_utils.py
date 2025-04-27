import pytesseract
from PIL import Image
import pdfplumber

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_image(image_file):
    pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text
