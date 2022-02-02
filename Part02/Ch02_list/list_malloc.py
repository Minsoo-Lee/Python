rows = int(input("rows:"))
cols = int(input("cols:"))
lst = []

# general
for row in range(rows):
    lst += [[0] * cols]
    
# implication
lst1 = []
lst1 = [ ([0] * cols) for row in range (rows)]