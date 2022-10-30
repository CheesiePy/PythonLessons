
"""
בתוך לולאת while
1. קבלו קלט מהמשתמש
2. הוסיפו אותו לרשימה חיצונית 
3. אם הקלט הוא QUIT צאו מהלולאה
4. הדפיסו את הרשימה
"""

# i = 0
# ### True = 1, False = 0

# x = 10

# while x:
#     print("hello")
#     x -= 1



counter = 0
user_input = ""
command_list = []
while user_input.lower() != "quit":
    user_input = input("Please enter you command: ")
    if(user_input.lower() == "add"):
        amount = input("enter the amount you would like to add")
        if amount.isdigit():
            counter += int(amount)
        else:
            print("can only add integer values")
            continue
    if(user_input.lower() == "print"):
        print(counter)






















# while(x):
#     print(x)
#     x += 1





# while True: 
#     print(i)
#     if i == 10:
#         break
#     i += 1
    