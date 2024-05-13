# 외계인의 기타 연주

import heapq
import sys

N, P = map(int, sys.stdin.readline().split())

guitar = dict()
count = 0
for i in range(N):
    jul, prat = map(int, sys.stdin.readline().split())
    if jul in guitar:
        #print(f"현재 올려져있는 최고 프랫 = {-guitar[jul][0]}, 내가 치려는 프랫 = {prat}")
        if -guitar[jul][0] > prat:  # 현재 줄의 프랫이 내가 치려는 프렛보다 높은 음이면
            while -guitar[jul][0] > prat:
                heapq.heappop(guitar[jul])
                count += 1
                #print("손 하나 뗌")
                if len(guitar[jul]) == 0:
                    break
            if len(guitar[jul]) != 0 and -guitar[jul][0] != prat:
                heapq.heappush(guitar[jul], -prat)  # 최대힙
                count += 1
                #print("손 추가")
            elif len(guitar[jul]) == 0:
                heapq.heappush(guitar[jul], -prat)  # 최대힙
                count += 1
                #print("손 추가")
        else:
            if -guitar[jul][0] != prat:
                heapq.heappush(guitar[jul], -prat)  # 최대힙
                count += 1
                #print("손 추가")
    else:  # 현재줄에 등록된 기록이 아무것도 없다면
        guitar[jul] = [-prat]
        count += 1
        #print("손 추가")

print(count)
