n = int(input("enter the number of students: "))

students = {}

for i in range(n):
    line = input("enter the details: ").split()
    name = line[0]
    marks = float(line[1])
    students[name] = marks

topper = max(students, students.get(name))
average = sum(students.values()) / n

print(topper)
print(average)