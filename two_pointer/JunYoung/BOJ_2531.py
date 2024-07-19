# 회전 초밥
# 투포인터이긴 한데, 완전 탐색 아닌강..?

import sys

N, d, k, c = map(int, sys.stdin.readline().split())

yummy = []

for _ in range(N):
    yummy.append(int(sys.stdin.readline()))

for i in range(k-1) : # 원형인척 이어 붙이기
    yummy.append(yummy[i])

start = 0
end = k-1
answer = 0

while end<len(yummy):
    # 몇 종류의 초밥이 있는지 보기 위함
    distinct_set = set(yummy[start:end+1]) #list->set으로 만드는 거의 비용이 얼마나 되지?
    #print(yummy[start:end+1])
    #print(distinct_set)

    diff_num = len(distinct_set)
    if c not in distinct_set: # 쿠폰이 다른 종류의 초밥이면 +1
        diff_num += 1

    # 먹을 수 있는 가짓수가 더 많으면 정답에 저장
    if diff_num>answer:
        answer= diff_num

    # 매번 수행
    start +=1
    end +=1

print(answer)




