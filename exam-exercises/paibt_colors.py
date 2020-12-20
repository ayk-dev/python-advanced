from collections import deque

string = deque(input().split())
main_colors = ['red', 'yellow', 'blue']
secondary = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}

found_colors = []
temp_secondary = []

while len(string) > 0:
    first = string.popleft()
    if not string:
        if first in main_colors:
            found_colors.append(first)
        continue

    last = string.pop()
    if (first + last) in main_colors:
        color = first + last
        found_colors.append(color)
    elif (last + first) in main_colors:
        color = last + first
        found_colors.append(color)
    elif (first + last) in secondary.keys():
        color = first + last
        temp_secondary.append(color)
        found_colors.append(color)
    elif (last + first) in secondary.keys():
        color = last + first
        temp_secondary.append(color)
        found_colors.append(color)
    else:
        first = first[:-1]
        last = last[:-1]
        middle = len(string) // 2
        if last:
            string.insert(middle, last)
        if first:
            string.insert(middle, first)


for color in temp_secondary:
    if secondary[color][0] not in found_colors or secondary[color][1] not in found_colors:
        found_colors.remove(color)

print(found_colors)
