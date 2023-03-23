# 배열 돌리기
# n은 홀수!

import sys
from collections import deque

answer = []
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, d = map(int, sys.stdin.readline().split())

    arr = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        arr[i] = list(map(int, sys.stdin.readline().split()))

    rotate = int(d / 45)

    if rotate < 0:
        for r in range(-rotate):
            temp = deque()
            for step in range(4):
                # print(step)
                if step == 0:  # 좌우 대각선(위->아래) -> 가로선(좌->우)
                    for i in range(n):
                        temp.append(arr[i][i])
                    # print(temp)
                    for i in range(n):
                        temp.append(arr[int((n + 1) / 2) - 1][i])
                        arr[int((n + 1) / 2) - 1][i] = temp.popleft()
                    step += 1
                elif step == 1:  # 가로선(좌->우) -> 우좌 대각선(아래->위)
                    # print(temp)
                    for i in range(n):
                        temp.append(arr[n - 1 - i][i])
                        arr[n - 1 - i][i] = temp.popleft()
                    step += 1
                elif step == 2:  # 우좌 대각선(아래->위)-> 세로선(아래->위)
                    # print(temp)
                    for i in range(n):
                        temp.append(arr[n - 1 - i][int((n + 1) / 2) - 1])
                        arr[n - 1 - i][int((n + 1) / 2) - 1] = temp.popleft()
                    step += 1
                elif step == 3:  # 세로선(아래->위) -> 좌우 대각선(아래->위)
                    # print(temp)
                    for i in range(n):
                        arr[n - 1 - i][n - 1 - i] = temp.popleft()
    else:
        for r in range(rotate):
            temp = deque()
            for step in range(4):
                if step == 0:  # 좌우 대각선 -> 세로선(위->아래)
                    for i in range(n):
                        temp.append(arr[i][i])
                    # print(temp)
                    for i in range(n):
                        temp.append(arr[i][int((n + 1) / 2) - 1])
                        arr[i][int((n + 1) / 2) - 1] = temp.popleft()
                    step += 1
                elif step == 1:  # 세로선(위->아래) -> 우좌 대각선
                    # print(temp)
                    for i in range(n):
                        temp.append(arr[i][n - i - 1])
                        arr[i][n - i - 1] = temp.popleft()
                    step += 1
                elif step == 2:  # 우좌 대각선-> 가로선(우->좌)
                    # print(temp)
                    for i in range(n):
                        temp.append(arr[int((n + 1) / 2) - 1][n - 1 - i])
                        arr[int((n + 1) / 2) - 1][n - 1 - i] = temp.popleft()
                    step += 1
                elif step == 3:  # 가로선(우->좌) -> 좌우 대각선(아래->위)
                    # print(temp)
                    for i in range(n):
                        arr[n - 1 - i][n - 1 - i] = temp.popleft()

    answer += arr

for i in answer:
    for j in i:
        print(j, end=' ')
    print()

#흠 temp 이용정도?