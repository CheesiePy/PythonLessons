# functions with parameters


# single line comment  (#)
"""
multi line comment(""" """)
"""


# a parameter is a variable that is used to pass data into a function
# an argument is the actual value of the variable that is passed to the function

## code example
def juicer(fruit="apple"):
    print(fruit, 'juice')

## the return keyword is used to return a value from a function
def crazy_func(a): # a is a parameter
    """
    param a: string
    return: string
    """
    return a.swapcase() 

def only_even(number):
    mylist = []
    for i in range(number):
        if i % 2 == 0:
            mylist.append(i)
    return mylist    
        
def only_three(given_list):
    mylist = []
    for i in given_list:
        if i % 3 == 0:
            mylist.append(i)
    return mylist


## home work 
"""
צרו פונקציה שמקבלת מספר ומחזירה רשימה עם כל המספרים שמתחלקים גם ב2 וגם 3 בלי שארית
"""



## the main function is used to call other functions and to run the program
def main():
    mylist = only_even(100)
    list1 = [i for i in range(100)]
    
    x = only_three(list1)
    print(x)
    #print(juicer(x))
    #print(crazy_func(x)) # x is the argument that is passed to the function
main()
