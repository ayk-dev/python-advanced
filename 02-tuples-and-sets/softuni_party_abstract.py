class Party:
    def __init__(self):
        self.__invited_guests = set()
        self.__attended_guests = set()

    def invite_guests(self, reservation_number):
        self.__invited_guests.add(reservation_number)

    def guests_attend(self, reservation_number):
        self.__attended_guests.add(reservation_number)

    def get_unattended_status(self):
        unattended = self.__invited_guests.difference(self.__attended_guests)
        print(len(unattended))
        print('\n'.join(sorted(unattended)))


n = int(input())

party = Party()

for _ in range(n):
    party.invite_guests(input())

while True:
    command = input()
    if command == 'END':
        break
    guest = command
    party.guests_attend(guest)

party.get_unattended_status()
