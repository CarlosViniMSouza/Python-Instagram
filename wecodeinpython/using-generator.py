#Method 1
lists = [1, 2, 3, 4, 5,
         6, 7, 8, 9]

print(sum(num for num in lists))
# It's not very practical.

#Method 2
print(sum(range(10)))