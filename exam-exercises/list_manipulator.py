from collections import deque


def list_manipulator(nums, *args):
    queue = deque(nums)
    cmd, position, *others = args
    if cmd == 'add':
        if position == 'beginning':
            queue = others + list(queue)
        elif position == 'end':
            for el in others:
                queue.append(el)

    elif cmd == 'remove':
        if others:
            count = others[0]
            if position == 'beginning':
                for i in range(count):
                    queue.popleft()
            elif position == 'end':
                for i in range(count):
                    queue.pop()
        else:
            if position == 'beginning':
                queue.popleft()
            elif position == 'end':
                queue.pop()

    return list(queue)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

