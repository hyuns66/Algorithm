# 암기왕

import sys

T = int(sys.stdin.readline())
answer = []
for _ in range(T):
    N = int(sys.stdin.readline())
    note1 = set(map(int, sys.stdin.readline().strip().split()))

    M = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().strip().split()))

    for i in note2:
        if i in note1:
            answer.append(1)
        else:
            answer.append(0)


for i in answer:
    print(i)

# set는 순서가 입력한 대로 들어가지 않는 듯하다. 왜 자동 오름차순으로 들어가지?
# 실수: T에 대한 처리를 안해줌.
# ? 이분 탐색?