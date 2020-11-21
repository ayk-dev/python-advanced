n = int(input())

student_records = {}
for _ in range(n):
    name, grade = input().split(' ')
    if name not in student_records:
        student_records[name] = []
    student_records[name].append(float(grade))

for student, values in student_records.items():
    average_grade = sum(values) / len(values)
    grades = ' '.join(map(str, ['{:.2f}'.format(val) for val in values]))
    print(f'{student} -> {grades} (avg: {average_grade:.2f})')
