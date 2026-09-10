"""c=bool(" ")+34-4
print(c)
str="python"
print(str[0])

print(str[len(str)-1])
print(str[-1])

print(str[-len(str)])

for i in range(len(str)):
    print(str[i])
for j in range(-len(str),0):
    print(str[j])

for s in str:
    print(s)

Str="python in GLA CL2"
# print(Str)
# print(Str[::])
print(Str[-5:9:-1])
print(Str[-100:100])

from sys import argv
# print(argv[0])
# print(argv[1])
# print(argv[2])
# print(argv[3])
print(len(argv))

print("Python"+" in GLA CL2")
print("python"*5)
print(3.5*"python")

s1=input("enter the string")
s2=input("enter the second string")
output= "same" if s1==s2 else " not same"
print(output)

s1=" Amit Singh "
print(len(s1))
print(len(s1.lstrip().rstrip()))

s="python is a programming language. Python is easy to learn. Python is used in AI ML"
print(s.find("zython"))
print(s.index("Python",35))
print(s.rfind("Python"))
print(s.rfind("Zython"))
print(s.rindex("Python"))

output= "yes" if s.find("Python")!=-1 else "NO"
print(output) 
output= "yes" if "Python" in s else "No"
print(output)
s="python is a programming language. Python is easy of learn. Python is used in AI ML"
print(id(s))
s1=s.count("Python")
print(id(s))
print(s1)

for i in s:
#     print(i,s.count(i),end=" ") if s.count(i)>14 else None

s="Rajesh, Suresh, Ram, Mayank"
s1=s.split(",")
# print(s1)
# print(s,type(s))
# print(type(s.split(",")))

for item in s1:
    print(item, s1.count(item),end=",")

dob=input("enter the Dob")
# year=dob.split("/")
# print(year[2])
print(dob[dob.rfind("/")+1:])

l=["22","11","2024"]
s="/".join(l)
print(s)

s="Amit Kumar"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

print(s.isupper())
print(s.islower())
print(s.istitle())
print(s.isalpha())
print(s.isalnum())
print(s.isdigit())
print(s.isidentifier())
print(s.isprintable())
print(s.isnumeric())

valu=input("enter the value")
a=eval(valu) if valu.isnumeric() else valu
print(a)

place="Delhi"
name="Amit"
s="{} is a good boy. He studies in {}".format(place,name)
print(s)
s="{1} is a good boy. He studies in {0}".format(place,name)
print(s)
s="{b} is a good boy. He studies in {a}".format(a=place,b=name)
print(s)

s=f"{name} is a good boy. He studies in {place}"
print(s)


"""

"""
CODE2

s=input("enter the string")
for char in s:
   p=input("enter the word of that you have to find the occurance")
   print(p,"comes",s.count(p),"times in the string")

"""

"""s=input("enter the string")
p=" "
for char in s:
    if char not in p:
        p+=char,s.count(char)
    else:
        continue
    if s.count(char)>1:
        print(char,s.count(char),end=" ")
    """
        



s = input("enter the string")
s1=" "
for char in s.split():
    p=char[::2]
    

# s=input("enter the string")
# p=" "
# for char in s:
#     if char not in p and s.count(char)>1:
#         p+=char+ str(s.count(char))+" "
#     else:
#         continue
# print(p)

# s="thequickbrownfoxjumpsoverlazydog"
# sub=""
# for i in s:
#     if i not in sub and s.count(i)>1:
#         sub+=i + " " + str(s.count(i)) + " "
# print(sub.strip())

    