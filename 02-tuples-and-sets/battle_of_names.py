n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    word = input()
    ascii_value = 0
    for ch in word:
        ascii_value += ord(ch)
    value = ascii_value // i
    if value % 2 != 0:
        odd_set.add(value)
    else:
        even_set.add(value)

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)

elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)

elif sum(odd_set) < sum(even_set):
    result = odd_set.symmetric_difference(even_set)

battle_of_names = ', '.join(map(str, result))
print(battle_of_names)

