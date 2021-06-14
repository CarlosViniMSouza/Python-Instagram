def Function(Parameter):
    return Parameter

Function = lambda Parameter : Parameter

def Add(a, b):
    return a+b

print(Add(5, 7))

Add = lambda a, b : a + b
print(Add(6, 8))