# 블랙잭

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
numComb = list(itertools.combinations(num, 3))

sumZip = []
for i in numComb:
    s = 0
    for n in i:
        s += n
    sumZip.append(s)

sumZip.sort()

for i in range(len(sumZip)):
    if sumZip[i] > M:
        i = i-1
        break

# print(sumZip)
print(sumZip[i])

# 젤 마지막 범위를 살피지 못했다.
# 제일 끝까지 갔을 때도 sumZip[i] > M인게 없을 수 있고, 그때는 그냥 젤 마지막 요소를 출력하면 되는데 이 부분을 빠뜨렸다.
