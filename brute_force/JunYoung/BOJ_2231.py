# 분해합

import sys

N = int(sys.stdin.readline())

g_dict = {}
start = N - len(str(N)) * 9
if start < 0:
    start = 0
for i in range(start, N+1):  # 이 범위 측정이 키 포인트! 처음엔 (1, 1000000)
    sum_num = i
    for j in range(0, len(str(i))):
        #print(j)
        sum_num += int(str(i)[j])
    #print(g_dict.get(sum_num))
    if g_dict.get(sum_num) is None:
        #print(sum_num)
        #print(i)
        g_dict[sum_num] = i

if g_dict.get(N) is None:
    print(0)
else:
    print(g_dict[N])

# 0이 예외 케이스였다.
# 그리고 생성자가 없을 때 0을 출력하는 걸 깜박함.
