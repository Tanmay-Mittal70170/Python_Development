# Using Packing and Unpacking of tuples: 

L=[]

for x in range(3):
    rollno=int(input("enter the roll no"))
    name=input("enter the name")
    email=input("enter the email")
    phone=int(input("enter the phone number"))
    t=rollno, name, email, phone
    L.append(t)

for r,n,e,p in L:
    print("%5d %-15s %20s %10d"%(r,n,e,p))