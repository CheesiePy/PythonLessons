
def encrypt(data, key):
    encrypt_data = ""

    for index in data:
        index_val = ord(index)
        range_val = 0

        if index_val >= 65 and index_val <= 90: # Capital letters 
            range_val = 65
        else: # small letters
            range_val = 97

     
        fixed_val = ((index_val - range_val) + key) % 25 + range_val


        if index_val != 32:
            encrypt_data += chr(fixed_val)
        else:
            encrypt_data += " "
    
    return encrypt_data



def decrypt(e_data, key):
    decrypt_data = ""

    for index in e_data:
        index_val = ord(index)
        range_val = 0

        if index_val >= 65 and index_val <= 90: # Capital letters 
            range_val = 65
        else: # small letters
            range_val = 97

     
        fixed_val = ((index_val - range_val) - key) % 25 + range_val


        if index_val != 32:
            decrypt_data += chr(fixed_val)
        else:
            decrypt_data += " "
    
    return decrypt_data




command = ""
while command != "quit":
    command = input("please enter your command: ")
    edata = encrypt(command, 2)
    print("encrypt :" , edata)
    print("decrypt :", decrypt(edata, 2))


