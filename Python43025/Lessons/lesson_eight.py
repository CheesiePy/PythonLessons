# width = 16
# height = 9
# scaler = 2
# for row in range(height*scaler):
#     for col in range(width*scaler):
#         print("*", end=" ")
#     print()

# print(height*scaler, width*scaler , height*width)

"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""


# size = 10
# for i in range(size): # run 9 times
#     for j in range(size): # run 9 x 9 times
#         print("0", end=" ") #-> 0 0 0 0 0 0 0 0 0
#     print()




""" 
X 0 0 0 0 0 0 0 0 
0 X 0 0 0 0 0 0 0 
0 0 X 0 0 0 0 0 0
0 0 0 X 0 0 0 0 0
0 0 0 0 X 0 0 0 0
0 0 0 0 0 X 0 0 0
0 0 0 0 0 0 X 0 0
0 0 0 0 0 0 0 X 0
0 0 0 0 0 0 0 0 X
"""


# size = 9
# for i in range(size):
#     for j in range(size):
#         if i == j:
#             print("X", end=" ")
#         else:    
#             print("0", end=" ")
#     print()

""" 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 X 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
"""

size = 21

for i in range(size):
    for j in range(size):
        if i == j and i == size//2:
            print("X", end=" ")
        else:
            print("0", end=" ")    
    print()







# for jelly in range(9): # run 8 times
#     for jam in range(9): # run 8 x 8 times = 64
#         if jelly == 0 or jelly == 8 or jam == 0 or jam == 8:
#             print("M", end=" ")
#         else:    
#             print("0", end=" ")
#     print()
