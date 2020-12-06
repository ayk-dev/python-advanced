# If the command is "Odd": Print the sum of the Odd numbers multiplied by the length of the initial list.
# If the command is "Even": Print the sum of the Even numbers multiplied by the length of the initial list.

command = input()
numbers = [int(x) for x in input().split()]

commands = {
    'Odd': sum([x for x in numbers if x % 2 != 0]) * len(numbers),
    'Even': sum([x for x in numbers if x % 2 == 0]) * len(numbers)
}

print(commands[command])

