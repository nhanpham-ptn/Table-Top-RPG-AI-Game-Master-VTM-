from pdf2image import convert_from_path
import pytesseract
from pathlib import Path

pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

def extract_text(pdf_path):
    text = ""
    images = convert_from_path(pdf_path, poppler_path = "Story\\poppler\\poppler-25.12.0\\Library\\bin")

    for i, img in enumerate(images):
        print(f"Processing page {i}")
        text += pytesseract.image_to_string(img, config="--oem 3 --psm 6")

    return text

def chunk_text(text, size=4000):
    return [text[i:i+size] for i in range(0, len(text), size)]

#-------------------------------------------------------------------------------------------------------------------------#
 
def reference():
    BASE_PATH = Path(r"Backend\Services\Story\Books")

    for book in BASE_PATH.iterdir():
        material = chunk_text(extract_text(f"{book}"))
        output_file = BASE_PATH / f"{book.stem}.txt"
        with open(output_file, "w", encoding="utf-8") as lore:
            for i, chunk in enumerate(material):
                lore.write(f"--- CHUNK {i} ---\n")
                lore.write(chunk)
                lore.write("\n\n")



