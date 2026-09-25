# Question2: To print the number of perticular word in a string 

s=input("enter the string")
for char in s:
   p=input("enter the word of that you have to find the occurance")
   print(p,"comes",s.count(p),"times in the string")

#Method 2

s=input("enter the string")
p=" "
for char in s:
    if char not in p:
        p+=char,s.count(char)
    else:
        continue
    if s.count(char)>1:
        print(char,s.count(char),end=" ")