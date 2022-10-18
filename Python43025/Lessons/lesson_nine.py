counter = 0
my_var = "AvivAmasterProgrammerInTheMaking"

print("the value of counter:", counter) # -> 0



for i in my_var:
    counter += 1
    print(i, end="\n")

print(counter)


"""
compartors:

a == b # is a equal to b?
a != b # is a not equal to b?
a > b # is a greater than b?
a < b # is a less than b?
a >= b # is a greater than or equal to b?
a <= b # is a less than or equal to b?


"""


data_base = {
    "user": "arthuristhking@gmail.com",
    "password": "15898201",
}



user = "arthuristhking@gmail.com"
password = "XXXX" # -> 0123456789
# brote force attack
for i in range(10): # -> 0
    for j in range(10):# -> 0
        for k in range(10):# -> 0,1
            for l in range(10): # -> 0,1,2,3,4,5,6,7,8,9
                for t in range(10): # -> 0,1,2,3,4,5,6,7,8,9
                    for y in range(10): # -> 0,1,2,3,4,5,6,7,8,
                        for u in range(10):
                            for z in range(10):
                                password = str(i) + str(j) + str(k) + str(l) + str(t) + str(y) + str(u) + str(z)
                                if password == data_base["password"]:
                                    print("password hacked:", password)



# if user == data_base["user"] and password == data_base["password"]:
#     print("Welcome to the system")



# print(counter != len(my_var))


# for i in ["python", "lesson"]:
#     print("the value of i[0]: ", i[0])


