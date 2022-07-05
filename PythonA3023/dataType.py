##--data type--##


"""
lesson Tools:

type(a) = the type fuction return the data type of a,

print(a) = print(a) to the console

"""


number = 12345678





# ----- exple ----#

def main():
    # ----primitives----#
    a = 15    # integer or int for sort a whole number
    b = "a"   # str/char -!!! in python we str or string type to reprianct a single charicter or a string of charicters
    c = 15.4  # float a decimal point number
    d = True  # boolean or bool for short is a binaty type being ethier one for true or zero for false
    print("----------------")
    print(a, b, c, d)
    print("----------------")
    print(type(a), type(b), type(c), type(d))
    for i in range(5):
        print("----------------")


main()
