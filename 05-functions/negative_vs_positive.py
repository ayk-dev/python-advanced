numbers = [int(x) for x in input().split()]

negatives = list(filter(lambda x: x < 0, numbers))
positives = list(filter(lambda x: x > 0, numbers))

print(sum(negatives))
print(sum(positives))

negatives_abs_values = [abs(x) for x in negatives]
if sum(negatives_abs_values) > sum(positives):
    print(f'The negatives are stronger than the positives')
else:
    print(f"The positives are stronger than the negatives")