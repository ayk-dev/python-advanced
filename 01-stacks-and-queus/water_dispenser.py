from collections import deque

water_quantity = int(input())

water_queue = deque()
while True:
    line = input()
    if line == 'Start':
        break
    water_queue.append(line)

while True:
    command = input()
    if command == 'End':
        break

    if command.isdigit():
        liters = int(command)
        person_to_get_water = water_queue.popleft()
        if water_quantity >= liters:
            print(f'{person_to_get_water} got water')
            water_quantity -= liters
        else:
            print(f'{person_to_get_water} must wait')

    elif 'refill' in command:
        liters = int(command.split(' ')[-1])
        water_quantity += liters

print(f'{water_quantity} liters left')