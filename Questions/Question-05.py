#Question 5: To check whether the student is pass or fail and also print his/her grade:

name=input("enter the name")

english=int(input("enter the marks of English"))
hindi=int(input("enter the marks of Hindi"))
maths=int(input("enter the marks of maths"))
science=int(input("enter the marks of science"))
geography=int(input("enter the marks of geography"))
History=int(input("enter the marks of History"))

sum=english+hindi+maths+science+geography+History
avg=sum/6

print(name,"sum of marks",sum)
print(name,"average of marks",avg)

if avg>=90 and avg<100:
    print(name,"Grade A+")
elif avg>=80 and avg<89:
    print(name,"Grade A")
elif avg>=70 and avg<79:
    print(name,"Grade B+")
elif avg>=60 and avg<69:
    print(name,"Grade B")
elif avg>=45 and avg<59:
    print(name,"Grade C")
elif avg>=33 and avg<44:
    print(name,"Grade D")
else:
    print(name,"Grade Fail")

if avg>33:
    print(name,"IS PASSED")
else:
    print(name,"IS FAILED")