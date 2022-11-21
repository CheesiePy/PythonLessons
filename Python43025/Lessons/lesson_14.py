# # varubles & data types 


# # my friends say "hello" 

# # string
# a = "hello"
# b = 'hello'
# ab = 'my friends say "hello"'
# # boolean
# t = True
# f = False
# # int / float
# n = 5
# fl = 0.5

# # operator
# """
# a = 
# a + b
# a * b
# a - b
# a ** b
# a % b
# a / b
# a // b

# a += b  a = a + b
# a -= b  a = a - b

# """

# # comperators 

# """
# a > b
# a < b
# a >= b
# a <= b
# a == b
# a != b
# """

# # logical operators

# """
# not(A)
# A or B -> 
# A and B -> 
# """
# # a = 3
# # b = "hello python!"
# # print(a == b or a != b)  ## always true! 
# # print(a == b and a != b) ## always false!
# # print((not a) or a) ## always true
# # print((not a) and a) ## always false


# a = 10
# b = 15
# c = 20

# if not a > b or b < c:
#     print("hey!")


# #conditinals 

# # if statment
# condition = a > b

# condition2 = a + b < b + c

# if condition:
#     print("the condition")

# # if else statment 
# if condition:
#     print("c was true")
# else:
#     print("c was false")

# # if elif else statement

# sun = 10
# moon = "hello world"

# if condition:
#     print("c was true")
# elif condition2:
#     print("c2 was true, and c was false")
# elif sun > moon:
#     print("goyava")
# elif moon*2 < 3:
#     print("banana!!!")            
# else:
#     print("c & c2 was false")        


# if condition:
#     print("v")
# if condition2:
#     print("w")  

# # switch case / match case 
# # later


# # loops!!

# # while loops!

# i = 0
# while i < 10:
#     print("heyy!")
#     i += 1

# # for in range()
# start = 0
# stop = 500
# jump = 5
# for i in range(start, stop, jump):
#     print(i)

# # # nested loops 
# for i in range(5): # run 5 

#     for j in range(5): # 5 x 5
#         print(i, j)

#         print("crazyyyyyyy")

# ## functions !! 

def f(): # function defention 
    print("a")
    print("b")

# f() # function call! 

# def g(a,b):
#     print(a + b)

# g(5,6)    

# for i in range(5):
#     g(i, 5)

def h(a, b):
    return a**b

x = h(2,2)
print(x)