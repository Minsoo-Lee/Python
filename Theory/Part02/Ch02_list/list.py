# list declare & init
scores = []
print("init:", scores)

scores = [30, "HI", 10.1123, "PHONE"]

# get index => use "if"
if "HI" in scores:
    index = scores.index("HI")
print("index:", index)

# modify
scores[1] = "hello"
print("mod:", scores)
print("list:", len(scores))

# iterate
for i in range(len(scores)):
    print(i, scores[i])
for i in scores:
    print(i)


    
