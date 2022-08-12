h, w = "Hello", "World"
symbols = "+-.,&$^987456314522,009)()())(!@#!~@#ADFGSDFG"

print("#-------IQ level1-----------")

print("Hello+World")
print("Hello,World")
print("Hello|World")
print("Hello\World")
print("Hello%World")

print("#-------End IQ level1-----------")


print('#-------IQ level2---------------')


print(h, w, sep=",")
print(h, w, sep="|")
print(h, w, sep="\\")
print(h, w, sep="END")
print(h, w, sep=' ')

print("#-------End IQ level2-----------")

print('#-------IQ level3---------------')

for i in symbols:
    print(h, w, sep=i)

print("#-------End IQ level3-----------")

# 1. להכין רשימה של שמות
# 2. ליצור לולאה אשר אומרת בוקר טוב ולילה טוב לכל שם ברשימה
# 3. קודם הוא יגיד לכולם בוקר טוב ואחר כך הוא יגיד לכולם לילה טוב

# Bonus - > שלב 3 לעשות בלולאה 1