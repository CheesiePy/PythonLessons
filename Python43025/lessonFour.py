# range function parameters:
start = 1  # start is the first number in the range
stop = 51  # stop is the last number in the range
jump = 1  # jump is the number to add to the start number each time the loop iterates

## for loops and range function
for i in range(start, stop, jump):
    print(i, end='\t')

# notes:

# \ back slash
# / forward slash

# print parameters:
# sep = " " # separator
# end = "\n" # end of line
# \n new line
# \t tab


# WRONG: split(mystring)
# x = mystring.split()


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

# lesson Three homework solution:

seporators = "+-.,&$^987456314522"
# slow way:
# myfriend = "yoav may maor"
# mylinelist = mylongstr.split('\n')
# mywordlist = mystr.split()

# better way:
mywordlist = "yoav may maor".split()

temp_str = ""  # temporary string that will be used to build the final string

for i in range(len(mywordlist)):
    if i % 2 != 1:
        mystr += mywordlist[i] + " "

print(mystr)

# lists:
mylist = [1, 2, 2, '5', 'saba']  # list of different types of data
print(len(mylist))  # length of the list

maylist = [mylist]  # nested list

print(*maylist)  # * unpacks the list

print(mylist, *mylist, sep="+")  # * unpacks the list and prints it

# * -> dereferance the list

# iterate over a list:
for i in mylist:
    print(i)

print("----")

# iterate over a list with index:
for i in range(len(mylist)):
    print(mylist[i])

print("----")


start = 0
stop = len(mystr)
jump = 1

print(mylist[::-1])                 # reverse the list

print(temp_str[start:stop:jump])    # slice the string

print(mystr[stop:start:-jump])      # reverce order its like [::-1]

print(temp_str[::-1])               # reverse the string
