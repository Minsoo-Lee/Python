# 이진 탐색
# 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
# 시간 복잡도 : O(logN)

from configparser import BasicInterpolation


array = []

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
n = 10
target = 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    
n = 10
target = 7
array = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]
result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)