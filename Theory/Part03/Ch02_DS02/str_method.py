# split()
str = "Hi John, I'm going to school"
lst = str.split() # seperate blank
print(type(lst))
print(lst)
lst = str.split("i")
print(lst)

# substring search
# endswith(str)
str = input("write Python src ")
if str.endswith(".py"):
    print("CORRECT")
else:
    print("WRONG")
# startswith(str)
str = "2021-03-04.txt"
if str.startswith("2021"):
    print("CORRECT")
else:
    print("WRONG")