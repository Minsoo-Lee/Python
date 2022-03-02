n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # a는 오름차순 정렬 수행
b.sort(reverse=True) # b는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    # a의 원소가 b의 원소보다 크거나 같을 때 반복문 탈출
    else:
        break

print(sum(a)) # a의 모든 원소의 합을 출력