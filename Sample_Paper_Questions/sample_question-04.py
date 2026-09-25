#Question: Write a Python program to check whether a given year is a leap year. A year is a
# leap year if: 
# • It is divisible by 4 but not by 100, or 
# • It is divisible by 400. 



year=int(input("enter the year"))

if year%4==0 and year%100!=0:
    print(year,"is a leap year")

elif year%400==0:
    print(year,"is a leap year")
    
else:
    print(year,"is not the leap year")