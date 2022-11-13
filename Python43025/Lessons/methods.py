# ## string methods
# # string methods are functions that are called on a string

# # 1. string.upper() - returns a copy of the string with all the characters in uppercase
# a = "hello"
# b = a.upper()
# print(b) # same as print(a.upper())

# # # 2. string.lower() - converts all characters to lowercase
# a = "HELLO"
# print(a.lower())

# # # 3. string.title() - capitalizes the first letter of each word
# a = "hello world how are you"
# print(a.title())

# # 4. string.capitalize() - capitalizes the first letter of the string
# a = "hello world"
# print(a.capitalize())

# # # 5. string.strip() - removes all leading and trailing whitespace
a = "     v    hello world    v   "


b = "Adam"
c = "A D A M"
d = " Adam "

# side note ord() -> return the unicode 
# print(ord("1"))



# print(len(b)) # 4
# print(len(c)) # 7
# print(len(d)) # 6
# print(b == c) # False
# print(b == d) # False
# print(b == d.strip()) # True
# print(type(b)) ## <class 'str'>



# print(a)
# print(a.strip())

# 6. string.replace(old, new) - replaces all occurrences of old with new
#string are immutable 
# a = "hello world"
# print(a)
# print(a.replace("world", "python"))

# # # 7. string.split() - splits the string into a list of substrings
# a = "hello world"
# print(a.split())

# # 8. string.join(list) - joins the elements in the list into a string
a = ["hello", "world" , "myfriends", "$$$"]
b = "~~~"
# print(b.join(a))

# 9. string.find(substring) - returns the index of the first occurrence of substring
a = "Lorem ipsum, dolor sit world amet consectetur adipisicing elit. Enim ipsam sunt et incidunt adipisci rerum perspiciatis quos non ea aut, id assumenda maxime eius a aliquid world possimus doloribus tempore ratione?"
w = "world of great great warcraft great great great great great great war of "

start = w.find("warraft")
stop = len(w)
print(w[start:stop])

