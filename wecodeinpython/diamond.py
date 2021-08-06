def prisme(n):
    #top part:
    for i in range(n):
        print((n-i-1)*" ", end="")
        print((2*i+1)*"*")
    #lower part:
    for i in range(n-1, -1, -1):
        print((n-i-1)*" ", end="")
        print((2*i+1)*"*")

prisme(5)