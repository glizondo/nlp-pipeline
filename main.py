# pip install -r requirements.txt

import re
from pathlib import Path
from typing import List, Any
from docx import Document

file_path = Path(str(r"document.docx"))


def read_doc():
    doc = Document(str(file_path))
    text_array = []
    for paragraph in doc.paragraphs:
        phrase = paragraph.text.split('.')
        text_array.extend(phrase)
    print(text_array)
    tokenization(text_array)


def tokenization(text_array) -> list[Any]:
    pattern = r'\w+|[^\w\s]'
    tokens = []
    for phrase in text_array:
        found_tokens = re.findall(pattern, phrase)
        tokens.extend(found_tokens)
    print(tokens)


read_doc()
