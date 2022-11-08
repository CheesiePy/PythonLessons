x = "hello"
y = "world"

"""
1. קבלו קלט מהמשתמש 
2. הוסיפו את האות הראשונה של הקלט לרשימה 

"""
# for xPhone_12123 in range(5):
#     print(xPhone_12123)


# for jelly in range(5):
#     print(jelly)





# for i in range(5):
#     print("jelly")


# print(i)





#range(9) מחזיר תווך של מספרים מ 0 - 9 לא כולל 9   

my_list = [] ## יצרנו רשימה ריקה בשם המשתנה my_list
for i in range(5): ## לולאת for רצה חמש פעמים
    user_input = input("Enter a word: ") # קולטים קלט מהמשתמש ושומרים אותו בשתנה user_input
    mychar = user_input[0] # המשתנה שלנו מחזיק את האות הראשונה מהחרוזת שקיבלנו מהמשתמש!
    my_list.append(mychar) # שם את האות הראשונה ששמנו במשתנה מיצ'אר ברשימה שהגרנו קודם

print(my_list)

# mylist = []
# mystr = "Noam"
# mystr2 ="Aviv"
# mylist.append(mystr2)
# mylist.append(mystr)
# print(mylist)


"""
בתוך לולאת while
1. קבלו קלט מהמשתמש
2. הוסיפו 
"""