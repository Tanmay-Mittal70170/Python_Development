#Question: Print This pattern:

#*#*#*
#*#*#
#*#*
#*#
#*

for x in range(1,6):
    for y in range(5,x-1,-1):
        if y%2==0:
            print("#",end="")
        else:
            print("*",end="")
    print()