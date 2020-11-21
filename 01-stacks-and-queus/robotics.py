from collections import deque
from datetime import datetime, timedelta

robots = input().split(';')

for i in range(len(robots)):
    robot = robots[i].split('-')

    robots[i] = {
        'name': robot[0],
        'process_time': int(robot[1]),
        'available_at': 0
    }

start_time = datetime.strptime(input(), '%H:%M:%S')

items = deque()

while True:
    next_item = input()
    if next_item == 'End':
        break
    items.append(next_item)

current_time = 0
time = 1

while len(items) > 0:
    current_time += time
    item = items.popleft()
    for robot in robots:
        # check first available robot
        if robot['available_at'] <= current_time:
            # Robot is available
            robot['available_at'] = current_time + robot['process_time']
            robot_name = robot['name']
            time_started = (start_time + timedelta(seconds=current_time))
            print(f'{robot_name} - {item} [{time_started.time()}]')
            break # if we got available robot
    else:
        items.append(item)






