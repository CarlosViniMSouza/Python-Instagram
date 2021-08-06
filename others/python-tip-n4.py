# don't this:

"""
x = input("Enter a word: ")
y = input("Enter a word: ")
z = input("Enter a word: ")
print(x)
print(y)
print(z)
"""

# do this:

x, y, z = input("Enter words: ").split()
print(x + "\n" + y + "\n" + z)