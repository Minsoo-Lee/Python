# call by reference : list, dictionary와 같은 mutable object 사용

def change(li):
    print("change_before :", li)
    print("change_before_id :", id(li))
    li += [100, 200]
    print("change_after :", li)
    print("change_after_id :", id(li))
    
list = ["Hi", 1, 3, 1, 1.1]
print("before :", list)
print("before_id :", id(list))
change(list)
print("after :", list)
print("after_id :", id(list))
