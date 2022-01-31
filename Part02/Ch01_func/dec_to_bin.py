def decTObin(num):
    binary = ""
    
    while num != 0:
        value = num % 2
        if value == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        num = num // 2
        print("num :", num)
    return binary

decNum = int(input())
print(decNum, decTObin(decNum))
