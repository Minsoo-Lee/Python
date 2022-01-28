user_list = ["이민수", "김연아", "손연재", "박길수", "지창욱"]
pw = "1234"

id = input("ID : ")
if id in user_list:
    password = input("PW : ")
    if password == pw:
        print("WELCOME")
    else:
        print("WRONG")
else:
    print("SIGN IN")