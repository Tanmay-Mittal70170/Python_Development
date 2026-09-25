#Question 13: To Print the Pattern given:

#0 
#0 1 
#0 1 2 
#0 1 2 3 
#0 1 2 3 4 

for x in range(1,6):
    for y in range(x):
        print(y,end="")
    print()


#To print this:

# 1
# 22
# 333
# 4444
# 55555

for x in range(1,6):
    for y in range(x):
        print(x,end="")
    print()