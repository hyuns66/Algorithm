import sys

N, M = map(int, sys.stdin.readline().split())

boxNum = 0
boxCurrent = []

if N > 0:
    books = list(map(int, sys.stdin.readline().split()))
    for i in range(len(books)):
        # 각 책에 대해서
        flag = False
        start = max(0, boxNum-1)
        for j in range(start, len(boxCurrent)):
            left = M - boxCurrent[j]
            if left >= books[i]:
                boxCurrent[j] += books[i]
                flag = True
                break
        if not flag:
            boxNum += 1
            boxCurrent.append(books[i])

print(boxNum)

# 책을 차례대로 넣어야한다는 게, 더 큰 숫자의 책이 앞의 상자에 들어가지 못한다(?)는 거다.
