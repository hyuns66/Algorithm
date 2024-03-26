import sys

N,K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
prefix_sum = dict()
prefix_sum[0] = 1   # 누적합 그 자체로 K를 만족하는 경우
answer = 0
for i, a in enumerate(A):   # 누적합 배열생성
    if i != 0:
        A[i] = A[i-1] + a
for a in A:
    num = a - K     # 누적합에서 a - num = K 가 되어야 하므로 (a가 큰 누적합 num이 작은 누적합, a는 알고 num을 구하는게 목적)
    if num in prefix_sum.keys():
        answer += prefix_sum[num]
    if a in prefix_sum.keys():
        prefix_sum[a] += 1
    else:
        prefix_sum[a] = 1
print(answer)