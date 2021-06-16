quant = 'ABCDE'

ip_str = 'Hy, my name is Carlos'
ip_str = ip_str.casefold()

count = {}.fromkeys(quant, 0)

for char in ip_str:
    if char in count:
        count[char] += 1
    print(count)
