# 영화감독 숌

import sys

N = int(sys.stdin.readline())
theEnd = []

num = 666
while len(theEnd) < N:
    #print(num)
    if '666' in str(num):
        theEnd.append(num)
        #print(str(num) + "추가됨")
    num += 1

print(theEnd[N-1])

# <의견>
# 뭔가 666이라는 규칙이 있었어서, num = 666부터 1씩 늘려서 일일히 다 체크하는 게
# 비효율적이고, 시간 초과가 날 것이라고 예상했는데.. 그렇게 풀기는 했다!
# 더 좋은 방법 없을까?