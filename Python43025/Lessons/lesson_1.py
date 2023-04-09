# data types 

# str 

f = "hello worldz"

second = "Hello World"



f_first_letter = f[0]

key = 2


# allowed values [65 - 90], [97 - 122]

# Z - 90
# 90 - 65 = 25
# (27 % 25) + 65 = 67 


encrypt_f = ""

for index in f:
    index_val = ord(index)
    range_val = 0

    if index_val >= 65 and index_val <= 90: # Capital letters 
        range_val = 65
    else: # small letters
        range_val = 97

     
    fixed_val = ((index_val - range_val) + key) % 25 + range_val




    if index_val != 32:
        encrypt_f += chr(fixed_val)
    else:
        encrypt_f += " "
    


print(encrypt_f)






print(f_first_letter)

# ord(char) -> ascii value 

# chr(ascii) -> char with given value

print(ord('a'))

print(chr(97))

