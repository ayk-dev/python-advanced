from collections import deque

players_queue = deque(input().split())
n_toss = int(input())

while len(players_queue) > 1:
    players_queue.rotate(-n_toss)
    removed = players_queue.pop()
    print(f'Removed {removed}')

print(f'Last is {players_queue.pop()}')