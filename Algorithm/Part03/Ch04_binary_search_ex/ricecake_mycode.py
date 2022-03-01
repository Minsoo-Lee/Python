n, m = map(int, input().split())
d = list(map(int, input().split()))

def binary_search(array, start, end):
    mid = (start + end) // 2
    ddeok = [(x-mid) for x in array]
    for i in range(n):
        if ddeok[i] < 0:
            ddeok[i] = 0
    if sum(ddeok) == m or start > end:
        return mid
    elif sum(ddeok) < m:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)


print(binary_search(d, 0, max(d)))