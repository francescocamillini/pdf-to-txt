import argparse
from io import StringIO
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
import filetype
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed

parser = argparse.ArgumentParser(description='Extract text from pdf with OCR')
parser.add_argument('-i', '--input', required=True,
                    help="input folder")
parser.add_argument('-o', '--output',  required=True,
                    help="output folder")

args = parser.parse_args()


def extract_text(path: str):
    resource_manager = PDFResourceManager()
    fake_file_handle = StringIO()

    converter = TextConverter(
        resource_manager, fake_file_handle,  laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(path, 'rb') as f:
        pages = PDFPage.get_pages(
            f, caching=True, check_extractable=True)

        try:
            for page in pages:
                page_interpreter.process_page(page)
        except PDFTextExtractionNotAllowed as e:
            print("PDF text extraction not allowed.")
            return ""
        except Exception as e:
            print(e)
            print("Error extracting text from PDF.")
            return ""

        text = fake_file_handle.getvalue()
        converter.close()
        fake_file_handle.close()

        if text:
            return text.replace('\xa0', ' ').replace('\x0c', ' ').replace('\n', ' ')


def is_pdf(path: str) -> bool:
    print(path)
    if(filetype.guess(path) is None):
        return False
    return filetype.guess(path).extension == 'pdf'


input_folder = args.input
output_folder = args.output

pdf_files = [join(input_folder, f) for f in listdir(input_folder) if isfile(
    join(input_folder, f)) and is_pdf(join(input_folder, f))]


for pdf_file in pdf_files:
    print(pdf_file)
    text = extract_text(pdf_file)
    text_file = open(
        join(output_folder, Path(pdf_file).stem + '.txt'), 'w')
    text_file.write(text)
    text_file.close
