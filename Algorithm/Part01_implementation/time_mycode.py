# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요

time = [0, 0, 0]
n = int(input())
count = 0
while time[0] <= n:
    if "3" in str(time[0]) or "3" in str(time[1]) or "3" in str(time[2]):
        count += 1
    time[2] += 1
    if time[2] == 60:
        time[2] = 0
        time[1] += 1
    if time[1] == 60:
        time[1] = 0
        time[0] += 1
            
print(count)