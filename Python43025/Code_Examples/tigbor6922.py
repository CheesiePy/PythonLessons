def crazy_func(number):

    mylist = [] 
    for i in range(number):
        if i % 2 == 0 and i % 3 == 0:
            mylist.append(i)
    return mylist

x  = crazy_func(100)
x.append("mango")
print(x)


