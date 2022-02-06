# dictionary : key + value
# key has to be uneditable

dict = {1: "apple", 2: "tomato", 3: "orange"}
print(dict)

# get key
print("dict[1]", dict[1])
print("dict[1]", dict.get(1))

# key가 딕셔너리에 없으면 디폴트 값 사용
print("dict[5]", dict.get(5, "pineapple"))

# pop
dict.pop(3)
print(dict)
del dict[1]
print(dict)

# clear
dict.clear();
print(dict)