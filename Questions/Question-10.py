string=input("enter the string")
First=string[:4]
last=string[-3:]
index=string[2:7]
Every=string[::2]
reverse=string[::-1]

print("orginal",string)
print("First 3:",First)
print("Last 3:",last)
print("Index of 2-7",index)
print("Every 2 character",Every)
print("Reversed String",reverse)