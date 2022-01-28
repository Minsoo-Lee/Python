# 리스트
city = ["서울", "부산", "대구", "광주", "인천"]
print(len(city))
print(city)
print(city[2])

# 리스트는 해당 인덱스의 값 변경 가능
city[1] = "전주"
print(city)

# 리스트는 자료형에 국한되지 않고 여러 개 값 저장 가능
temp = ["대구", "부산", 100, 10.798]
print(temp)

name = input("name : ")
age = int(input("age : "))
address = input("address : ")
height = int(input("height : "))
weight = int(input("weight : "))
person = [name, age, address, height, weight]
print(person)