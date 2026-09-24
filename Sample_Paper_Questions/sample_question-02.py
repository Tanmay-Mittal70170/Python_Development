#Question: Write a Python program that takes a string input representing a number (e.g., "123.45")
#Convert it to int (truncate), float, and complex. Print each converted value along with its data type. 

number=input("enter the number")

decimal=float(number)
print(decimal,type(decimal))

integer=int(decimal)
print(integer,type(integer))

comp=complex(decimal)
print(comp, type(comp))