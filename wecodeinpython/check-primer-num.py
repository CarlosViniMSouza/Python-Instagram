num = int(input("Writinhg any number: "))

if num > 1:

    for i in range(2, num):
        if (num%i) == 0:
            print(num, "isn't not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "isn't a prime number!")