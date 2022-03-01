n, x = map(int, input().split())
num = list(map(int, input().split()))

def binary_search(arr, start, end):
    mid = (start + end) // 2
    if start > end:
        return -1
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search(arr, mid + 1, end)
    else:
        return binary_search(arr, start, mid - 1)
    
find = binary_search(num, 0, max(num))
start, end = find, find

while num[end] == find and end < len(num):
    end += 1
while num[start] == find and start >= 0:
    start -= 1
    
print(end - start + 1)