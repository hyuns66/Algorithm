# 서로소 평균

import sys
import math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())

answer = []
for i in range(N):
    if math.gcd(X, A[i]) == 1:  # 서로소이면
        answer.append(A[i])

answerAverage = 0.0
for i in answer:
    answerAverage += i
answerAverage = answerAverage / len(answer)
print(answerAverage)

"""
서로소를 판단하는 기준은 둘의 최대공약수가 1인 것을 기준으로 잡기!
나는 괜히 a,b (a<b)일때 b%a!=0이면 서로소라고 생각했는데,
이는 6,9인 경우 해당하지 않는다!
"""