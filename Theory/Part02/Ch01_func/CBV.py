# call by value
def change(num):
    num = num + 10
    print("inside :", num)
    print("inside id :", id(num))
    
# 파이썬에서는 모든 값들이 객체로 이루어져 있다.
n = 100
print("before :", n)
print("before id :", id(n))
change(n)
print("after :", n)
print("after id :", id(n))