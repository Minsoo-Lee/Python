def push(data, n):
    data.append(n)
    
def pop(data):
    if len(data) > 0:
        return data.pop()
    else:
        print("EMTPY STACK!")