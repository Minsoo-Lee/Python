scores = []
print("list:", scores)

# add
# append()
scores.append(30)
print("add:", scores)
scores.append("HI")
print("add:", scores)
scores.append(10.1123)
print("add:", scores)
print("list:", len(scores))
# insert()
scores.insert(1, "PHONE")
print("insert:", scores)
print("list:", len(scores))

# delete
# pop
element = scores.pop(0)
print("element:", element)
print("pop:", scores)
# remove
scores.remove("HI")
print("element:", element)
print("remove:", scores)
# del
del scores[0]
print("del:", scores)
#clear
scores.clear()
print("element:", element)
print("clear:", scores)