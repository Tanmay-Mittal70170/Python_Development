#Take the input as string and start and end index value then print the substring and reverse of it:

string=input("enter the string")
index=int(input("enter the start index"))
end_index=int(input("enter the end index"))

substring=string[index:end_index]
reverse=substring[::-1]
print("substring",substring)
print("reverse of substring",reverse)