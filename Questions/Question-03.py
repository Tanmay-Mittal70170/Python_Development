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
