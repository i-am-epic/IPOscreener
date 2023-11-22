import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.

    Parameters:
    - pdf_path (str): Path to the PDF file.

    Returns:
    - str: Extracted text.
    """
    text = ""
    with fitz.open(pdf_path) as pdf_doc:
        for page_num in range(pdf_doc.page_count):
            page = pdf_doc[page_num]
            text += page.get_text()
            print(page_num)
    return text

# Example Usage
pdf_path = '1699876097528.pdf'
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text)
