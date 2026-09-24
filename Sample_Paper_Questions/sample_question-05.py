n=int(input("enter the number you have to print the table"))

for i in range(1,11):
    if i==7:
        break
    else:
        print(n,"x",i,"=",n*i)