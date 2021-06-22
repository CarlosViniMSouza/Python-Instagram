a, b, c, d = 18, 14, 12, 16
condition = [a >= 0, b <= 10, c >= 12, d <= 20]

if any(condition):
    print("Condition okay")
else:
    print("Condition not-okay")

if all(condition):
    print("Condition okay")
else:
    print("Condition not-okay")