n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0] 
    tail = array[1:] 
    left = [x for x in tail if x <= pivot] 
    right = [x for x in tail if x > pivot] 
    return quick_sort(left) + [pivot] + quick_sort(right)

a = quick_sort(a)
b = quick_sort(b)
b.reverse()

print(a)
print(b)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(a)
print(b)        