# 선택 정렬
# 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것
# 시간 복잡도 : O(N^2)

import time

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)

start_time = time.time()

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap
    
end_time = time.time()
print(array)
print(end_time - start_time)