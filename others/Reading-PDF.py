# pip install pymupdf

import fitz

with fitz.open("file.pdf") as pdf:
    text = ""

    for pg in pdf:
        text += pg.getText()

print(text)