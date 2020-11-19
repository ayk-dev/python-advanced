from collections import deque

green_light = int(input())
free_window = int(input())

cars_queue = deque()

counter = 0
is_crashed = False

while True:
    command = input()
    if command == 'END':
        break

    if command == 'green':
        time_left = green_light
        if cars_queue:
            car = cars_queue.popleft()
            next_car = deque(car)
            while time_left > 0:
                time_left -= 1
                if not next_car:
                    if cars_queue:
                        car = cars_queue.popleft()
                        next_car = deque(car)
                    else:
                        break
                next_car.popleft()
            if next_car:
                free_timer = free_window
                while free_timer > 0:
                    if next_car:
                        next_car.popleft()
                    else:
                        break
                    free_timer -= 1

            if next_car:
                is_crashed = True
                character_hit = next_car.popleft()
                break
    else:
        car = command
        cars_queue.append(car)
        counter += 1
    if is_crashed:
        break

if is_crashed:
    print('A crash happened!')
    print(f'{car} was hit at {character_hit}.')
else:
    print(f'Everyone is safe.')
    print(f'{counter - len(cars_queue)} total cars passed the crossroads.')
