# global variable : defined out of function

def test():
    print(text);

text = "study python" # global_var
test()

# When change global_var : add global keyword
def test1():
    # tell interpreter "i will use global_var [text1] inside function"
    global text1
    print(text1)
    text1 = "Study Python"
    print(text1)
    
text1 = "Study Java"
test1()
print(text1)