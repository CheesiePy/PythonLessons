#import - keyword (להוסיף ספרייה לקוד שלנו)
# import random (ייבא לקוד שלי את כל ספריית ראנדום)

# pip install {שם הספריה} (אם לא נמצאה הספרייה אפשר להתקין אותה עם השורת פקודה הבאה בטרמינל) 
from random import randint

dice_dict = {
    1:"""
     _______
    |       |
    |       |
    |   o   |
    |       |
    |_______|""",
    2:"""
     _______
    |       |
    | o     |
    |       |
    |     o |
    |_______|""",
    3:"""
     _______
    |       |
    | o     |
    |   o   |
    |     o |
    |_______|""",
    4:"""
     _______
    |       |
    | o   o |
    |       |
    | o   o |
    |_______|""",
    5:"""
     _______
    |       |
    | o   o |
    |   o   |
    | o   o |
    |_______|""",
    6:"""
     _______
    |       |
    | o   o |
    | o   o |
    | o   o |
    |_______|"""
}

commend = ""
while False:
    
    # get user input
    commend = input("enter a number of dice you would like to roll or quit to exit: ")


    # exit condition
    if commend.lower() == "quit":
        print("thanks for playing")
        break
    
    # allowed non-digit first chars
    prefix = ["-","+"]

    # check if the user entered a number
    if commend.isdigit() or (commend[1:].isdigit() and commend[0] in prefix):
        number_of_rolls = abs(int(commend))
    else:
        number_of_rolls = 1

    # roll given number of dice    
    for i in range(number_of_rolls):    
        dice = randint(1,6)
        print(dice_dict[dice], end="")



def dice_builder(n):
    #posible
    top =    " _______ "
    botton = "|_______|"
    empty =  "|       |"
    mid =    "|   o   |"
    two =    "| o   o |" 
    left =   "| o     |"
    right =  "|     o |"     

    dice = ""

    dice += top + "\n" + empty + "\n"
    match n:
        case 1:
            dice += empty + "\n" + mid + "\n" + empty + "\n"
        case 2:    
            dice += left + "\n" + empty + "\n" + right + "\n"
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass

    dice += botton

    print(dice)


dice_builder(2)    