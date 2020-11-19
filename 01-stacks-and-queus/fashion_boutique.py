stack_of_clothes = list(map(int, input().split(' ')))
capacity = int(input())

racks_count = 1
sum_of_clothes = 0

while stack_of_clothes:
    one_piece = stack_of_clothes.pop()

    if sum_of_clothes + one_piece <= capacity:
        sum_of_clothes += one_piece
    else:
        racks_count += 1
        sum_of_clothes = one_piece

print(racks_count)

