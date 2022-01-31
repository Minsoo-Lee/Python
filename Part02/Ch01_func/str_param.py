# 문자열 전달

def change(string):
    string += "study"
    print("string :", string)
    print("string_id :", id(string))
    
msg = "HI, I "
print("before :", msg)
print("before_id :", id(msg))
change(msg)
print("after :", msg)
print("after_id :", id(msg))