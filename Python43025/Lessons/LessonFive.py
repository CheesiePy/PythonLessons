## Function in Python!

## Functions are a way to reuse code.

# if 5 > 2: ## condition -> True or False
#     print("V")

# for i in range(6): ## loop
#     print(i)


# while 1 > 2: ## loop - while loop - while condition is true
#     print("V")    

def greeting(): ## define a function  -> retrun string value
    name = input("Enter your name: ")
    if validate_greeting(name):
         return name
    else:
        return "John Doe"

def validate_greeting(name): ## define a function with parameters
    if not name.isalpha() or not len(name) < 3:
        return False
    else:
        return True               

def print_greeting():
    print("Hello", greeting())


def print_greeting_2(name="John Doe"): ## define a function with parameters
    print("Hello", name)

 



def main(): ## main function
    # home work define crazy_func function
    x = "maylindenberg"
    print(crazy_func(x)) # -> crazy_func return -> "MaYliNdEnGeR" this
main() ## main function call




