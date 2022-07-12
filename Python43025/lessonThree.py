# h, w = "Hello", "World" 
# symbols = "+-.,&$^987456314522,009)()())(!@#!~@#ADFGSDFG"



# print("#-------IQ level1-----------")
# print("Hello+World")
# print("Hello,World")
# print("Hello|World")
# print("Hello\World")



# print('#-------IQ level2------------')
# print(h,w, sep=",")  
# print(h,w, sep="|")
# print(h,w, sep="\\")  
# print(h,w, sep="END")
# print(h,w)        



# print('#-------IQ level3------------')
# h, w = "Hello", "World" 
# symbols = "+-.,&$^987456314522,009)()())(!@#!~@#ADFGSDFG%@#$@#$"
# for i in symbols:
#     print(h,w,h,w, sep=i) 


# # \ back slash 
# # / forward slash    







# ## WRONG: split(mystring)
# ## x = mystring.split()



mystr = "Hello my friends at progeeks python class"
seporators = "+-.,&$^987456314522"


mylist = mystr.split()
# print(mylist)






start = 0
stop = len(mystr)
jump = 1


# print(len(mylist)) # -> 7

# list1 = [1,2,2]

# maylist = [mylist]

# print(maylist) # -> 1  

# print(mylist, *mylist, sep="+")


## * -> dereferance

# for i in range(len(mylist)):
#     print(mylist[::-1])

print(mystr[stop:start:-jump]) ## reverce order its like [::-1]
print(mylist[start:stop:jump])

print(mystr[::-1])


# 1. להכין רשימה של שמות 
# 2. ליצור לולאה אשר אומרת בוקר טוב ולילה טוב לכל שם ברשימה
# 3. קודם הוא יגיד לכולם בוקר טוב ואחר כך הוא יגיד לכולם לילה טוב 

# Bonus - > שלב 3 לעשות בלולאה 1 