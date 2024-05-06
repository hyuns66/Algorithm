# 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1
# 지동이 방에 모기가 가장 많이 있는 시간대의 연속 구간 전체
# 여러 가지 방법이 있으면 가장 빠른 시작 시각 출력
import heapq

import sys
N = int(sys.stdin.readline())

h = []
for i in range(N):
    TE, TX = map(int,sys.stdin.readline().split())
    heapq.heappush(h, (TE, "E"))
    heapq.heappush(h, (TX, "X"))


max_mogi = 0
max_mogi_range = []
mogi = 0
while h:
    value, index = heapq.heappop(h)
    if index == "E": # 모기 진입시
        mogi += 1
    else: # 모기 진출시
        if mogi == max_mogi:
            max_mogi_range.append(value) # 현재모기가 맥스모기인데 줄여야할때 기록
        mogi -= 1

    if len(h)>0 and h[0][0] == value: # 다음께 동일한 시간대이면 동시에 수행
        continue

    #print(f"{value}시간, 모기수 = {mogi}")
    if mogi > max_mogi:
        max_mogi = mogi
        max_mogi_range = [value] # 모기가 맥스모기를 넘으면 시작점 기록

print(max_mogi)
print(*max_mogi_range[:2])