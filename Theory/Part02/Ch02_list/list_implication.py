# iterate
lst = [x for x in range(1, 11)]
print(lst)

# iterate + if
odd_lst = [x for x in range (1, 21) if x % 2 == 1]
print(odd_lst)

# double iterate
gugudan_lst = [i * j for i in range(2, 10) for j in range(1, 10)]
print(gugudan_lst, end = " ")
print()

# in str
lst = ["KOREA", "대한민국", "서울특별시", "한라산", "END"]
first_word = [word[0] for word in lst]
print(lst)
print(first_word)

# Cross Product
lst = ["White", "Brown", "Black"]
car = ["그랜저", "소나타", "스파크", "아반떼", "봉고"]

car_lst = [x + "-" + y for x in car
            for y in lst ]
print(car_lst)