class LikedList:
    def __init__(self):
        self.node = None

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

list = LikedList()
list.node = Node("Monday")

new = Node("Tuesday")
list.node.next = new

new1 = Node("Wednesday")
new.node = new1

print(new)

# Output: <__main__.Node object at 0x00000163B70B0C40>