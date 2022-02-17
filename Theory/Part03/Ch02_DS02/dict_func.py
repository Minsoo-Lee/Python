scores = {"국어": 80, "수학": 95, "영어": 80}

# iteration
# get keys
for subject in scores.keys():
    print(subject, end = " ")
print("")

# get values
for score in scores.values():
    print(score, end = " ")
print("")

# get keys & values
for subject in scores.items():
    print(subject, end = " ")
print("")

# comprehension
triples = { x : x * x * x for x in range(6)}
print(triples)

# sort
dict = {"pens": 6, "bags": 1, "books": 5, "bottles": 4, "coins": 3, "cups": 2}
print(dict)
lst = list(dict.keys())
print(lst)
# sort keys
lst = sorted(dict)
print(sorted(dict))
print(lst)
# sort values
lst = sorted(dict.values())
print(sorted(dict.values()))
print(lst);
print(sorted(dict, key=dict.__getitem__))