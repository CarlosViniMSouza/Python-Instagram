# before : pip install pyshortners

import pyshorteners

# original URL:
url = 'https://www.instagram.com/CarlosViniMSouza'

# load lib:
lib = pyshorteners.Shortener()

# creat shortener URL:
shortURL = lib.tinyurl.short(url)

# show result:

print(f"Your web address: {shortURL}")