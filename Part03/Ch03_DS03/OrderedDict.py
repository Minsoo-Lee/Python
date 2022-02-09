# OrderedDict : Dictionary has order

# Dictionary
dic = {}
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400

for k, v in dic.items():
    print(k, v)
    
# OrderedDictionary
from collections import OrderedDict

dic = OrderedDict()
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400