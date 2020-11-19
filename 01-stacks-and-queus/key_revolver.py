from collections import deque

price_per_bullet = int(input())
size_of_barrel = int(input())
bullet_stack = list(map(int, input().split(' ')))
lock_queue = deque(map(int, input().split(' ')))
value = int(input())

out_of_resources = False
money_spent = 0

index = 1
while len(lock_queue) > 0 and len(bullet_stack) > 0:

    current_lock = lock_queue.popleft()
    bullet = bullet_stack.pop()
    money_spent += price_per_bullet
    if money_spent > value:
        lock_queue.appendleft(current_lock)
        out_of_resources = True
        break

    if bullet <= current_lock:
        print('Bang!')
    else:
        print('Ping!')
        lock_queue.appendleft(current_lock)
    if index % size_of_barrel == 0 and len(bullet_stack) > 0:
        print('Reloading!')
    index += 1

if out_of_resources or len(lock_queue) > 0:
    print(f"Couldn't get through. Locks left: {len(lock_queue)}")
else:
    money_earned = value - money_spent
    print(f"{len(bullet_stack)} bullets left. Earned ${money_earned}")

