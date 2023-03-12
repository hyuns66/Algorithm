"""
달력을 365 길이의 list로 표현
그리고 각 날짜에 밑에 일정이 표시된 길이를 할당
예를들어 문제에 있는 그림의 경우 리스트는
[1, 1, 2, 3, 2, 2, 1, 1, 0, 1, 2, 0]
이렇게 하면 원래 달력의 모양과는 조금 다른 데이터가 되긴 하지만 넓이를 구하는데는 문제없음

<원본 데이터>
0 0 0 0 0 0       0 0
    0 0   0 0 0     0
      0 0

<list 데이터>
0 0 0 0 0 0       0 0
    0 0 0 0 0 0     0   -> 여기서 최대 높이, 길이 가지고 직사각형 넓이 구해서 합
      0                 -> 힙 사용해서 한번에 그래프 그래고 인덱스 1부터 쭉 훑으면 되니까 시간복잡도 O(N)
"""

import sys
import heapq

N = int(sys.stdin.readline())
heap = []
calendar = [0] * 365
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (start, start - end))    # 시작점 기준 최소힙, 길이기준 최대힙으로 동작하도록 heappush

while heap:
    h = heapq.heappop(heap)
    start = h[0]
    dist = -h[1]
    for i in range(start-1, start + dist):
        calendar[i] += 1

height = 0
length = 0
answer = 0
for i in range(365):
    if calendar[i] == 0:
        answer += height * length
        height = 0
        length = 0
    else:
        length += 1
        height = max(height, calendar[i])
answer += height * length
print(answer)
