# 마인크래프트

import sys
from collections import Counter

N, M, B = map(int, sys.stdin.readline().split())

area = []
for i in range(N):
    area += list(map(int, sys.stdin.readline().split()))

c = Counter(area).most_common()
c.sort(key=lambda x:x[0], reverse=True)
#print(c)

target_level = max(area)

min_sec = sys.maxsize
answer_level = 0
while target_level >= 0:
    sec = 0
    block = B
    for i in c:
        diff = i[0] - target_level
        #print(f"{i} , target_level = {target_level}, diff = {diff}")
        if diff > 0:  # 뿌수기
            sec += 2 * i[1] * diff
            block += i[1] * diff
        elif diff < 0:  # 쌓기
            #print(f"필요한 블럭수 : {i[1] * abs(diff)} /가진 블럭 수 : {block}")
            if i[1] * abs(diff) <= block:
                sec += i[1] * abs(diff)
                block -= i[1] * abs(diff)  # 블럭 사용한 만큼 빼주기
            else:
                sec = -1  # 실패 표시
                break
    if sec == -1:
        target_level -= 1
        continue
    else:
        if sec < min_sec:
            min_sec = sec
            answer_level = target_level
        target_level -= 1

print(f"{min_sec} {answer_level}")

## [반례] ##
# 2 2 1000
# 0 0
# 1 63
# answer: 126 1

# input:
# 3 3 0
# 23 21 17
# 44 18 29
# 25 16 32
# answer: 90 25