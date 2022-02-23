# 알파벡 대문자와 숫자로만 구성된 문자열이 입력으로 주어집니다.
# 이 때, 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에
# 모든 숫자를 더한 값을 이어서 출력합니다.

input_data = input()
alpha, n, is_num = [], 0, False

for ch in input_data:
    if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
        alpha.append(ch)
    elif ord(ch) >= ord('0') and ord(ch) <= ord('9'):
        n += int(ch)
        is_num = True

alpha.sort()
if (is_num == True):
    alpha.append(str(n))
for ch in alpha:
    print(ch, end = "")