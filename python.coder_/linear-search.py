array = [1, 5, 10, 15]
x = 1
n = len(array)

def linearSearch(array, n, x):
    for i in range(1, n):
        if(array[array[i] == x]):
            return i
    return -1

result = linearSearch(array, x, n)

if(result == -1):
    print("Element not were possible found")
else:
    print("Element found: ", result)