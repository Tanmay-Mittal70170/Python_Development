#Check for palindrome:


string=input("enter the string")
if string==string[::-1]:
    print("string is palindrome")
else:
    print("not the palindrome ")