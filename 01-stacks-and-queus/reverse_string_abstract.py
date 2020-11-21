class Stack:
    def __init__(self, items):
        self.__items = items

    def append(self, item):
        return self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)


stack = Stack(list(input()))

while stack.size() > 0:
    item = stack.pop()
    print(item, end='')
print('')