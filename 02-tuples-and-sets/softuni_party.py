count = int(input())

invited_guests = set([input() for _ in range(count)])

guest_attended = set()
while True:
    command = input()
    if command == 'END':
        break
    guest = command
    guest_attended.add(guest)

unattended = invited_guests.difference(guest_attended)
print(len(unattended))

print('\n'.join(sorted(unattended)))
