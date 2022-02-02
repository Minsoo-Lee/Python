# read file
data = []
fp = open("C:\\test.txt", mode="r", encoding="UTF-8")
print(fp)
# readlines() : read whole thing in file
for line in fp.readlines():
    # strip() : trim both side " " / remove "\n" in fileIO
    data.append(line.strip())
print("FILE START")
print(data)
fp.close()

# write file
# w : 덮어쓰기, a : 이어쓰기
fp = open("C:\\test.txt", mode="w", encoding="UTF-8")
fp.write("We study Python")
fp.write("I study Python")