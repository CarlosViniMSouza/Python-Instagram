def is_anagram(s, s1):

    if len(s) != len(s1):
        return False
    else:
        for i, j in zip(s, s1):
            if i != j:
                return False
            return True

s = input("Writing any world: ")
s1 = input("Writing any world: ")

s = sorted(s.lower())
s1 = sorted(s1.lower())
res = is_anagram(s, s1)

if res == True:
    print("This words is Anagram")
else:
    print("This words isn't Anagram")