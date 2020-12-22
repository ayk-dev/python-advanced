from collections import deque

customers = deque(int(c) for c in input().split(', '))
taxis = deque(reversed([int(t) for t in input().split(', ')]))

total_time = 0

while len(taxis) > 0:
    first_customer = customers.popleft()
    last_taxi = taxis.popleft()
    if last_taxi >= first_customer:
        total_time += first_customer
    else:
        customers.appendleft(first_customer)

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(list(map(str, customers)))}')


