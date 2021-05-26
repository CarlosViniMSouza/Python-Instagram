# See what be the output in this program:

dict1 = {
    1 : "fruit",
    2 : "vegetables",
    3 : "greens"
}

dict2 = {
    4 : "candys",
    5 : "sweets",
    6 : "treats"
}

dict3 = {
    7 : "juice",
    8 : "refri",
    9 : "lemonade"
}

# Now, add 1 dict in other dict:

dict2.update(dict3)
dict1.update(dict2)

# The result:
print(dict1.json())