# before: pip install easyocr

import easyocr as easy

# Define your native language:

reader = easy.Reader(['pt'])

# Read image:
res = reader.readtext('<your image>', paragraph = False)

# Intering result:
for result in res:
    print(f'Text Found:\n'
            f'\tPosition: {result[0]}\n'
            f'\tText: {result[1]}\n')

# Execute the script and see the result: