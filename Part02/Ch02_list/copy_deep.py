# deep copy

# 1. list()
scores = [10, 20, 30, 40, 50]
refer = list(scores)
print("scores_id:", id(scores))
print("refer_id:", id(refer))

refer[0] = 100
refer.append(-70)
refer.insert(1, -100)

print("scores:", scores)
print("refer:", refer)

# 2. deep module - deepcoopy() / copy()
import copy
scores = [10, 20, 30, 40, 50]
refer = copy.deepcopy(scores) 
refer2 = copy.copy(scores)      # deepcopy() == copy()
print("scores_id:", id(scores))
print("refer_id:", id(refer))
print("refer2_id:", id(refer2))

refer[0] = 100
refer.append(-70)
refer.insert(1, -100)

refer2[0] = -10
refer2.append(70)
refer2.insert(1, 100)

print("scores:", scores)    
print("refer:", refer)
print("refer2:", refer2)

# 3. indexing
scores = [10, 20, 30, 40, 50]
refer = scores[:]
print("scores_id:", id(scores))
print("refer_id:", id(refer))

refer[0] = 100
refer.append(-70)
refer.insert(1, -100)

print("scores:", scores)
print("refer:", refer)