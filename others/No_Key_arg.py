def study(*num):
    result = 0
    for i in num:
        result = result + i
    return result

print(study(1, 3, 9, 27))

# Output: 40