# Question: Problem Statement: Write a Python program that:
# 1. Takes a string as input.
# 2. Prints the string in reverse.
# 3. Counts the number of vowels. 
# 4. Replaces all spaces with an underscore _. 



string=input("enter the string")

vowels=0

reverse=string[::-1]

List_vowel=["a","e","i","o","u"]

print("reverse",reverse)

for vowel in string:
    if vowel.lower() in List_vowel:
        vowels+=1

    if vowel==" ":
        string=string.replace(vowel,"_")


print("Total Vowels",vowels)
print("New String",string)
