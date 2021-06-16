dict = {"var": 10,
        "arg": 15,
        "msg": "Helloo!"}

def sum(var, arg, msg):
    total = print(msg, "Your number is:", var+arg)
    return total

sum(**dict)