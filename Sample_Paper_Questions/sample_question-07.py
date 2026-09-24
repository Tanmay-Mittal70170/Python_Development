string=input("Enter the space sperated numbers").split()
List=[]

for number in string:
    Integer=int(number)

    if Integer not in List:
        List.append(Integer)

print(List)