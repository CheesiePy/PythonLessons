# h, w = "Hello", "World" 
# symbols = "+-.,&$^987456314522,009)()())(!@#!~@#ADFGSDFG"



# print("#-------IQ level1-----------")

# print("Hello+World")
# print("Hello,World")
# print("Hello|World")
# print("Hello\World")
# print("Hello%World")


# print('#-------IQ level2------------')
# print(h,w, sep=",")  
# print(h,w, sep="|")
# print(h,w, sep="\\")  
# print(h,w, sep="END")
# print(h,w, sep=' ')        



# print('#-------IQ level3------------')
# h, w = "Hello", "World" 
# symbols = "+-.,&$^987456314522,009)()())(!@#!~@#ADFGSDFG%@#$@#$"
# for i in symbols:
#     print(h,w, sep=i) 

# stop = 51  ### not including 50  0 -> n-1
# start = 1
# jump = 1
# for i in range(start,stop,jump):
#     print(i, end='\t')



# # \ back slash 
# # / forward slash    







# ## WRONG: split(mystring)
# ## x = mystring.split()



mystr = "Hello my friends at progeeks python class"

mylongstr = """Hello my friends at progeeks python class
Hello my friends at progeeks python class
Hello my friends at progeeks python class
Hello my friends at progeeks python class
Hello my friends at progeeks python class
Hello my friends at progeeks python class
Hello my friends at progeeks python class
Hello my friends at progeeks python class
"""

# # seporators = "+-.,&$^987456314522"

# # myfriend = "yoav may maor"
# mylinelist = mylongstr.split('\n')
# mywordlist = mystr.split()
# mystr = ""

# # for i in range(len(mywordlist)):
# #     if i%2 != 1:
# #         mystr +=  mywordlist[i] + " "
    
# print(mystr)









# print(len(mylist)) # -> 7

mylist = [1,2,2,'5', 'saba']
#print(len(list1))

maylist = [mylist]

# print(*maylist) 

# print(mylist, *mylist, sep="+")


## * -> dereferance

# for i in mylist:
#     print(mylist[i])

# print("----")

# for i in range(len(mylist)):
#     print(mylist[i])


# for i in range(len(mylist)):
#     print(mylist[::-1])

start = 0
stop = len(mystr)
jump = 1





print(mylist[::-1])


# print(mystr[start:stop:jump])

# print(mystr[stop:start:-jump]) ## reverce order its like [::-1]

# print(mystr[::-1])


# 1. להכין רשימה של שמות 
# 2. ליצור לולאה אשר אומרת בוקר טוב ולילה טוב לכל שם ברשימה
# 3. קודם הוא יגיד לכולם בוקר טוב ואחר כך הוא יגיד לכולם לילה טוב 

# Bonus - > שלב 3 לעשות בלולאה 1 