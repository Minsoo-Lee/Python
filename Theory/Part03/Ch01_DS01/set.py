# set : 요소들의 중복 허용 X, 순서 유지 X
# {...}로 구현

# 1. 세트는 입력순서와 동일하게 출력하지 않음
set1 = {2, 1, 34, 5, 3}
print(set1)

# 2. 세트는 중복을 허용하지 않는다.
set2 = {"Hi", "person", "car", "hello", "Hi"}
print(set2)

# 3. 값 추가 : add()
set3 = set()
set3.add("Spring")
set3.add("Summer")
set3.add("Fall")
set3.add("Winter")
print(set3)

# 4. 값 추가 : update() (리스트 사용)
set4 = set()
set4.update(["Person", 1, 34, 5, -10])
print(set4)

# 5. 값 삭제 : discard(), remove()
set4.discard("Person")
print(set4)

# 6. 값 삭제 : clear()
set4.clear()
print(set4)