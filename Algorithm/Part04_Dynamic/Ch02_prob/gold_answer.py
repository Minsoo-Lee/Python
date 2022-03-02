# 해결 아이디어
# 왼쪽 위에서 / 왼쪽 아래에서 / 왼쪽에서 오는 경우 3가지만 고려하면 된다.
# 3가지 경우 중에서 가장 많은 금을 가지고 있는 경우를 테이블에 갱신
# array[i][j] : i행 j열에 존재하는 금의 양
# dp[i][j] : i행 j열까지의 최적의 해
# 점화식 : dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
# 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크

for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼족에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)