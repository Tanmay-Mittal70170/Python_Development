# Question 1: TO Print the odd place letters of any into a new stirng:

s = input("enter the string")
for char in s.split():
    p=char[::2]
    print(p,end=" ")


s=input('enter the string')
a=""
a=a+s[::2]
print(a)


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
  
#Question 3: To add the repeated words in new string and tell now many time also if they are greater than 1:

s=input("enter the string")
p=" "
for char in s:
    if char not in p and s.count(char)>1:
        p+=char+ str(s.count(char))+" "
    else:
        continue
print(p)

#Method 2:

s="thequickbrownfoxjumpsoverlazydog"
sub=""
for i in s:
    if i not in sub and s.count(i)>1:
        sub+=i + " " + str(s.count(i)) + " "
print(sub.strip())

#Question 4: To check if # and * are equal print 0, if greater print positive number
# if less than than print a negative number

s=input("enter the string")

if s.count("#")==s.count("*"):
    print("0 The string has equal number of # and *")

elif s.count("#")>s.count("*"):
    print("1 The string has greater number of # than *")
    
else:
    print("-1 The string has less number of # than *")