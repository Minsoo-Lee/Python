# shallow copy
scores = [10, 20, 30, 40, 50]
refer = scores
print("scores_id:", id(scores))
print("refer_id:", id(refer))

refer[0] = 100
refer.append(-70)
refer.insert(1, -100)

print("scores:", scores)
print("refer:", refer)