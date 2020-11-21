from collections import deque

supermarket_queue = deque()

while True:
    input_line = input()
    if input_line == 'End':
        break

    elif input_line == 'Paid':
        while len(supermarket_queue) > 0:
            print(supermarket_queue.popleft())

    else:
        name = input_line
        supermarket_queue.append(name)

count_of_people_left = len(supermarket_queue)
print(f'{count_of_people_left} people remaining.')