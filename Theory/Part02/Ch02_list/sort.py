li = [80, 90, 100, -70, -50]
print("li:", li)
print("")
# sort() : change src, NONE return
li.sort()
print("li:", li)
print("")
# sorted() : X change src, new list return
li = [80, 90, 100, -70, -50]
li1 = sorted(li)
print("li:", li)
print("li1", li1)
print("")
# reverse : reverse order (sort X)
li = [80, 90, 100, -70, -50]
li.reverse()
print("li:", li)
print("")
# sort(reverse=True) : reverse sort
li = [80, 90, 100, -70, -50]
li.sort(reverse=True)
print("li:", li)
print("")
# sorted( , reverse=True)
li = [80, 90, 100, -70, -50]
li1 = sorted(li, reverse=True)
print("li:", li)
print("li1", li1)
print("")