## לולאה שאנחנו לא יודעים מראש כמה פעמים היא תחזור על עצמה 




#print(type(flag))

# for i in range(100):
#     if i % 3 == 0:
#         print(i)


from re import I


flag = True
counter = 0


# while flag:
#     counter += 1
#     print("Hello", end='')
#     if counter == 10  < 7:
#         flag = False
#         print("Goodbye")
#         break
#     if counter < 7:
#         print("Bye", end='')

#     else:
#         print("!")


#     print(counter)

## a = 97 z = 122
while flag:
    user_input = input("Enter a letter: ")
    if user_input == "Quit":
        flag = False
        break
    if len(user_input) > 1:
        print("Please enter only one letter")
        continue
    print("You entered: ", user_input)
    sypher = 3
    dest = ((ord(user_input) + sypher) % 26) + 97
    print(chr(dest))