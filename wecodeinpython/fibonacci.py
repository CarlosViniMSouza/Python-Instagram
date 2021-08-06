n = int(input("How many numbers do you want?: "))

n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Writing Numbers Positive!")
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < n:
        print(n1)
        same = n1+n2
        
        n1 = n2
        n2 = same
        count += 1