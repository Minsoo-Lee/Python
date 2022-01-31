def tuple_return():
    return 1, "안녕", 5

a, b, c = tuple_return()
tuple_variable = tuple_return()

print(a, b, c)
print(tuple_variable)
print(type(tuple_variable))

list = list(tuple_variable)
list.append("HI")
print(list)
print(type(list))