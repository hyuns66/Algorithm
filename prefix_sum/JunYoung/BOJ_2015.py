# 수들의 합 4
# 부분 합 중 합이 K인 것이 몇개나 있는지 구하시오.
import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
vals = list(map(int, sys.stdin.readline().split()))

dict = {0: 1} # 누적합을 기록해둘 딕셔너리
# 아무것도 선택하지 않았을 때의 누적합 0은 기본으로 하나 넣어둠.

sum = 0
count = 0
for i in range(N):
    sum += vals[i]

    # 1. 부분합이 K인 것이 있는 지 확인
    if sum - K in dict: # 지금가지의 누적합에서 K만큼 차이나는게 누적합 기록 딕셔너리에 있으면
        count += dict[sum - K] # 부분합이 K인 것이므로 그 수만큼 더해준다.

    # 2. 지금의 누적합을 딕셔너리에 기록
    if sum in dict:
        dict[sum] += 1
    else:
        dict[sum] = 1

print(count)
