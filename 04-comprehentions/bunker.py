# {category} - {item_name} - quantity:{item_quantity};quality:{item_quality}
bunker = {
    category: []
    for category in input().split(', ')
}
n = int(input())

count = 0
total_quality = 0
for _ in range(n):
    category, item, info = input().split(' - ')

    bunker[category].append(item)
    quan, qual = info.split(';')
    quantity = int(quan.split(':')[1])
    quality = int(qual.split(':')[1])
    count += quantity
    total_quality += quality

print(f'Count of items: {count}')
print(f'Average quality: {total_quality / len(bunker.keys()):.2f}')
for key, value in bunker.items():
    print(f'{key} -> {", ".join(value)}')