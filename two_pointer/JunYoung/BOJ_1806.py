# 부분합

import sys

N, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

prefix = [0 for _ in range(N)]

prefix[0] = data[0]
for i in range(1, N):
    prefix[i] = prefix[i - 1] + data[i]

start = 0
end = 0
answerLen = sys.maxsize
while (start <= end) and (end < N):
    sum = prefix[end] - (prefix[start - 1] if start - 1 >= 0 else 0)
    len = end - start + 1
    if sum >= S: #부분합 중에 가장 짧은 것의 길이를 원하니까 S를 넘었다면 start +=1
        if len < answerLen:
            answerLen = len
        start += 1
    else: #아직 안 넘었다면 더 많은 수가 필요하니까 end+=1
        end += 1
if answerLen==sys.maxsize:
    answerLen = 0

print(answerLen)
