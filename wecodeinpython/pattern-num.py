def pattern(num):

    for i in range(0, num):
        for j in range(1, i+2):
            print(j, end=" ")
        print()

    for i in range(num, 0, -1):
        for j in range(i-1, 0, -1):
            print(j, end=" ")
        print()

pattern(10) 