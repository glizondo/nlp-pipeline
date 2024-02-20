# pip install -r requirements.txt

import re
from pathlib import Path
from typing import List, Any
from docx import Document
import nltk

file_path = Path(str(r"document.docx"))
nltk.download('averaged_perceptron_tagger')
print("---Thanks to Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. "
      "O’Reilly Media Inc.---")


def pipeline():
    text_array = read_doc()
    tokens = tokenization(text_array)
    classification_tokens = classify_tokens(tokens)
    lemmatization_table = create_lemmatization_table()
    stop_words = {'be', 'the', 'can', 'to', 'at'}
    print_doc_without_stop_words(tokens, lemmatization_table, stop_words)


def read_doc():
    doc = Document(str(file_path))
    text_array = []
    for paragraph in doc.paragraphs:
        phrase = paragraph.text.split('.')
        text_array.extend(phrase)
    return text_array


def tokenization(text_array):
    pattern = r'\w+|[^\w\s]'
    tokens = []
    for phrase in text_array:
        found_tokens = re.findall(pattern, phrase)
        tokens.extend(found_tokens)
    print(f'Tokens {tokens}')
    return tokens


def classify_tokens(tokens):
    tagged = nltk.pos_tag(tokens)
    print(f'Classification tokens {tagged}')
    return tagged


def create_lemmatization_table():
    lemmatization_file = Path("lemmatization-en.txt")
    lemmas_dict = {}
    with lemmatization_file.open('r') as file:
        for line in file:
            parts = line.strip().split()
            base = parts[1]
            extension = parts[0]
            lemmas_dict[base] = extension
    return lemmas_dict


def print_doc_without_stop_words(tokens, lemmatization_table, stop_words):
    result_tokens = []
    lemma_stop_words_dict = {}
    for base, extension in lemmatization_table.items():
        if base in stop_words or extension in stop_words:
            lemma_stop_words_dict[base] = extension
    for token in tokens:
        if token in lemma_stop_words_dict.keys() or token in lemma_stop_words_dict.values():
            print(f'DELETED TOKEN: {token}')
        else:
            result_tokens.append(token)
    text = ''
    for word in tokens:
        if word == ',':
            text += '\n'
        else:
            text += ' ' + word
    print(text)


pipeline()
