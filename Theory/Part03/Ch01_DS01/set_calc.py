set1 = {10, 20, 30}
set2 = {10, 20, 30}

print("same?", set1 == set2)
print("diff?", set1 != set2)

# subset
set2 = {10, 20, 30, 40, 50, 60}
print("bubun?", set1 < set2)
print("bubun?", set1.issubset(set2))

# superset
print("superset?", set2.issuperset(set1))

#union
print("union?", set1.union(set2))
print("union?", set2.union(set1))

# intersection
print("intersection?", set1.intersection(set2))
print("intersection?", set2.intersection(set1))

# difference
print("diff?", set2-set1)
print("diff?", set2.difference(set1))
print("diff?", set1.difference(set2))

# all / any
set3 = {0, 20, 30, 40, 50, 60}
print("all?", all(set3))
print("any?", any(set3))

# disjoint : 집합이 처음부터 아예 다른지 확인
print("disjoint?", set2.isdisjoint(set1))