# Question 1: TO Print the odd place letters of any into a new stirng:

s = input("enter the string")
for char in s.split():
    p=char[::2]
    print(p,end=" ")

#Method 2:
s=input('enter the string')
a=""
a=a+s[::2]
print(a)
