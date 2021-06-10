import random
import string

low = string.ascii_lowercase
up = string.ascii_uppercase
digits = string.digits
sym = string.punctuation

together = low + up + digits + sym

length = 15
password = "".join(random.sample(together, length))

print("Your password is: ", password)