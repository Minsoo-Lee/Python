# hello()는 매개변수 2개를 가지지만 디폴트 인수가 있기 때문에
# 함수 호출시 name에 대응되는 인수 값만 가지고도 호출이 가능하다.

def hello(name, msg="HI"):
    print("HI " + name + ", " + msg)

hello("minsoo")
hello("minsoo", "bye")