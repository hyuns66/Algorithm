import sys
from collections import deque

N = (int)(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
b.sort()
# #####################################
bDeque = deque()    # 굳이 덱 안쓰고 b 리스트로 인덱스가지고 놀면서 해도 되긴 할건데
for i in range(N):  # 밑에서 그렇게했더니 알 수 없는 오류땜에 똑왜틀 되서 그냥 맘편하게 덱으로 구현
    bDeque.append(b[i])     # 리스트 그대로 덱으로 옮겨서 하나씩 popleft하면서 전체탐색


def maxLength(sum):
    idx = len(bDeque)-1
    while idx >= 2:
        max = bDeque[idx]
        if max < sum:
           return idx+1
        idx -= 1
    return 0


result = 0


while bDeque:       # popleft 하면서 탐색하기 때문에 bDeque 사라질 때 까지 반복
    if len(bDeque)>2:   # 길이가 2이하면 그냥 삼각수열로 친다
        temp = maxLength(bDeque[0]+bDeque[1])   # 가장 작은수 두개 합 구해서 최대값 비교, 최종 삼각수열 길이반환
        bDeque.popleft()    # 다음인덱스로 옮겨서 탐색
        if temp > result:
            result = temp   # 최대 길이 업데이트
    else:
        if result < len(bDeque):
            result = len(bDeque)
        break

print(result)
#####################################
# bSum = list()
#
# for i in range(N-1):    # realB[0]+realB[1], realB[1]+realB[2] , ~~~, realB[N-2]+realB[N-1]
#     sum = b[i] + b[i+1]
#     bSum.append(sum)   # 앞 부터 차례대로 2개씩 합 구해서 배열에 저장
#
# result = -1
#
# for i in range(N-1):
#     index = N-1
#     while bSum[i]>b[index]:
#         index -= 1
#         if index < 0:
#             break
#     temp = N - (i + N-(index+1))  # 삼각수열이 되기 위해 빠져야 하는 인덱스의 수(i + N-index)를 제외하고 남은 최소 삼각수열의 길이
#     if result < temp:
#         result = temp
#
# print(result)