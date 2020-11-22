def enter(vehicle):
    parking_lot.add(vehicle)


def exit_parking(vehicle):
    if vehicle in parking_lot:
        parking_lot.remove(vehicle)


count = int(input())

parking_lot = set()
operations = {
    'IN': enter,
    'OUT': exit_parking
}

for _ in range(count):
    direction, car = input().split(', ')
    operations[direction](car)

if len(parking_lot) > 0:
    print('\n'.join(parking_lot))
else:
    print('Parking Lot is Empty')