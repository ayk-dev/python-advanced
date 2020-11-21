from collections import deque

n = int(input())
petrol_amounts = deque()
pumps_distances = deque()

for _ in range(n):
    amount, distance = input().split(' ')
    petrol_amounts.append(int(amount))
    pumps_distances.append(int(distance))

index = None

for i in range(n):
    is_valid = True
    fuel = 0
    for _ in range(n):
        petrol = petrol_amounts.popleft()
        dist = pumps_distances.popleft()
        current = petrol - dist
        fuel += current
        if fuel < 0:
            is_valid = False
        petrol_amounts.append(petrol)
        pumps_distances.append(dist)
    if is_valid:
        index = i
        break
    petrol_amounts.append(petrol_amounts.popleft())
    pumps_distances.append((pumps_distances.popleft()))

print(index)





