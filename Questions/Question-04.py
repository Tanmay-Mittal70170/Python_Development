#Question 4: To check if # and * are equal print 0, if greater print positive number
# if less than than print a negative number

s=input("enter the string")

if s.count("#")==s.count("*"):
    print("0 The string has equal number of # and *")

elif s.count("#")>s.count("*"):
    print("1 The string has greater number of # than *")
    
else:
    print("-1 The string has less number of # than *")
