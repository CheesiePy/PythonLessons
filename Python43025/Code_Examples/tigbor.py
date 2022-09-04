"""
1. variubles
2. data types
3. input
4. loops
5. functions
"""

# 1. variables
var_name = "Tigbor"
var_age = 25

# 2. data types
# string, int, float, boolean *-> to be learn (list, tuple, dictionary)

# 3. input
name = input("What is your name? ")
print(name)


# 4. loops
name = "Adam is the man!"

for i in range(10):
    print(type(i))

for i in name: # by value
    print(i)    

for i in range(len(name)): # by index
    if i%2 == 0:
        print(i, end=" ")
        print(name[i])




