# 프린터 큐

import sys
from collections import deque

T = int(sys.stdin.readline())

importance = deque()
answer = []
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())

    importance = deque(map(int, sys.stdin.readline().split()))
    orderImportance = deque(sorted(importance, reverse=True))

    count = 0
    while True:
        if importance[0] == orderImportance[0]:
            count += 1
            if M == 0:
                answer.append(count)
                break
            else:
                orderImportance.popleft()
                importance.popleft()
                M -= 1
        else:
            importance.rotate(-1)
            if M == 0:
                M = len(importance) - 1
            else:
                M -= 1

for i in answer:
    print(i)

"""
새로운 정렬된 리스트를 반환하는 함수는 sorted 함수이고, 
리스트 자체를 정렬시켜버리는 것은 sort 함수입니다.
https://blockdmask.tistory.com/466
"""