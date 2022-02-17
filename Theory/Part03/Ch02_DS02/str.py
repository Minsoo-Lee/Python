# slicing
word = "Python"
word1 = word[0:3]
print(word1)
print(word[0:100])

# cmp
print("apple" < "banana")

# ord()
print(ord("a"))
print(ord("b"))

# chr()
print(chr(97))
print(chr(65))

# format
str = "{}b{}"
print(str.format("a", "c"))

# join()
str = ["a", "b", "c"]
print("!".join(str))

# partition
str = "minsoo.james1101@gmail.com"
print(str.partition("@"))

# count()
str = "aaaaaabc"
print(str.count("z"))

# find()
str = "apple"
print(str.find("p"))

# strip()
str = "    aaa   bbb    ccc   dddd   \t"
print(str.strip())
print(str.rstrip())
print(str.lstrip())