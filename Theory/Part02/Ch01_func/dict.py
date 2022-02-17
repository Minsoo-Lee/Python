# dictionary : key + value
# key : unique, value : modifiable
dicst = {"name" : "이민수", "age" : 14, "height" : 160}

def change(dic):
    print("change_before :", dic)
    print("change_before_id :", id(dic))
    dic["몸무게"] = 42
    print("change_after :", dic)
    print("change_after_id :", id(dic))
    
print("before :", dicst)
print("before_id :", id(dicst))
change(dicst)
print("after :", dicst)
print("after_id :", id(dicst))
