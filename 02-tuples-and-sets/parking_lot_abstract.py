class Parking:
    def __init__(self):
        self.__cars = set()

    def process_car(self, direction, car):
        if direction == 'IN':
            self.__cars.add(car)
        elif direction == 'OUT' and car in self.__cars:
            self.__cars.remove(car)

    def print_status(self):
        if self.__cars:
            print('\n'.join([reg_num for reg_num in self.__cars]))
        else:
            print('Parking Lot is Empty')


parking_lot = Parking()

count = int(input())
for _ in range(count):
    direction, reg_num = input().split(', ')
    parking_lot.process_car(direction, reg_num)

parking_lot.print_status()

