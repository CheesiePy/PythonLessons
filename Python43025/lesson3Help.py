#print("hello world")

mystring = "hello world"
# print(mystring)

my_list = mystring.split()
# # print(type(my_list))

# # print(my_list[0][-1])

# for char in mystring:
#     print(char)
# print("-----------")
# for str in my_list:
#     print(str)
# print("------------")
# for i in range(len(my_list)):
#     print()
#     for j in range(len(mystring)):
#         print(my_list[i], mystring[j], sep= ",", end="")

start = 0
stop = len(mystring)
jump = -2


        
single_char = mystring[0]     ## char in location 0
group_chars = mystring[::jump] ## chars in location 0 to 6 in steps of 1
print(group_chars)

print("-----------")
rev_str = mystring[::-1]        
rev_list =my_list[::-1]        
print(rev_str, rev_list, sep="+")        
        