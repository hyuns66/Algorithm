# 강의실 배정
# Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데,
# 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
# Ti <= Sj인 경우, i수업과 j수업은 같이 들을 수 있다!

import sys, heapq

h = []
N = int(sys.stdin.readline())
for i in range(N):
    Si, Ti = map(int, sys.stdin.readline().split())
    h.append((Si, "S"))
    h.append((Ti, "E"))

heapq.heapify(h)

count = 0
answer = 0
while h:
    time, type = heapq.heappop(h)
    if type == "S":
        count += 1
    else:
        count -= 1
    # print(f"({time},{type}) current count = {count}")
    if len(h) != 0 and h[0][0] == time:
        continue
    answer = max(answer, count)

print(answer)
