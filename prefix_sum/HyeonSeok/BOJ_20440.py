import sys
from collections import defaultdict

N = int(sys.stdin.readline())
history = defaultdict(int)
times = set()
for _ in range(N):
    e, x = map(int, sys.stdin.readline().split())
    times.add(e)
    times.add(x)
    history[e] += 1
    history[x] -= 1
    
time_list = sorted(list(times))
answer = [0, [0, 0]]
cnt = 0
flag = False    # True인 경우 현재 모기가 최대로 존재하는 상태
for time in time_list:
    cnt += history[time]
    if answer[0] < cnt:
        answer[0] = cnt
        answer[1][0] = time
        flag = True
    if flag and cnt < answer[0]:
        answer[1][1] = time
        flag = False
print(answer[0])
print(*answer[1])