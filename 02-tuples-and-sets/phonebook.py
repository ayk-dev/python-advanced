phonebook = {}

while True:
    input_data = input()
    if input_data.isdigit():
        n = int(input_data)
        break

    name, number = input_data.split('-')
    if name not in phonebook:
        phonebook[name] = ''
    phonebook[name] = number

for _ in range(n):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')