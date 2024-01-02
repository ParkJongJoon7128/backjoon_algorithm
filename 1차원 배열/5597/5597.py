students = [i for i in range(1, 31)]

for _ in range(28):
    number = int(input())
    students.remove(number)

print(min(students))
print(max(students))