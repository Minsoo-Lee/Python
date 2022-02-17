colors = ("red", "blue", "yellow")
print(colors)
print(type(colors))

numbers = (1, 2, 3, 4, 5)
print(numbers)

li = [1, 2, 3, 4, 5]
num = tuple(li)
print(li)
print(num)

# good
person = ("minsoo", 29, "chis")
(name, age, grade) = person

# return : return multiple values
def calc(r):
    area = r * 2
    cir = 2 * r * r
    return (area, cir)

# enumerate
score = [(80, 90), (90, 100), (100, 110)]
for i, score in enumerate(score):
    print(score)
    