
input1 = input().split()
input2 = input().split()

list1 = []
for num in input1:
    list1.append(int(num))

list2 = []
for num in input2:
    list2.append(int(num))


common = set(list1) & set(list2)
print("Common elements:", common)


squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print("Squares of even numbers:", squares)