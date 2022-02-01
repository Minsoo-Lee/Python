# sort str(base on unicode)
li = ["하와이", "폭포", "가나", "한국"]
li1 = sorted(li, key=str.lower)
print("li:", li1)

# seperate str
str = "Im Programming Professor living in Korea. Nice to meet you"
li = str.split()
print("li:", li)