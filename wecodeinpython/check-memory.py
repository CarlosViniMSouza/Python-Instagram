import sys

num = 1
string = 'ABCDE'
lists = [('CARLOS'), ('SOUZA')]

print(
    "num occupies (in kb):", sys.getsizeof(num), "\n"
    "string occupies (in kb):", sys.getsizeof(string), "\n"
    "lists occupies (in kb):", sys.getsizeof(lists), "\n"
)