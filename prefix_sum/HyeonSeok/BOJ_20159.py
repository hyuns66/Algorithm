import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
prefix_sum = list()

for n in range(N):
    i = n - 2
    if i < 0:
        prefix_sum.append(cards[n])
    else:
        prefix_sum.append(cards[n] + prefix_sum[i])

answer = prefix_sum[-2]     # 밑장빼기 안했을 때

for i in range(0, N-2, 2):
    pre_sum = prefix_sum[i]     # 지금까지 내가 받은 카드 누적합
    if i > 0:
        pro_sum_front = prefix_sum[-3] - prefix_sum[i-1]
    else:
        pro_sum_front = prefix_sum[-3]
    pro_sum_back = prefix_sum[-1] - prefix_sum[i+1]     # 밑장빼기 했을 때 내가 받아야 할 카드 누적합 (밑장빼기 안한 경우 상대방이 받을 카드)
    answer = max(answer, pre_sum + pro_sum_front)   # 밑장빼서 너주기
    answer = max(answer, pre_sum + pro_sum_back)    # 밑장빼서 내가갖기
answer = max(answer, prefix_sum[-1])    # 시작부터 밑장빼기
print(answer)