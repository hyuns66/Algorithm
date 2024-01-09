# 베스트셀러

import sys

N = int(sys.stdin.readline())
bestSeller = {}
for _ in range(N):
    bookName = sys.stdin.readline().strip()
    if bookName in bestSeller.keys():
        bestSeller[bookName] += 1
    else:
        bestSeller[bookName] = 1

bestSellNum = 0
for sell in bestSeller.values():
    if sell > bestSellNum:
        bestSellNum = sell

answer = []
for book in bestSeller.keys():
    if bestSeller[book] == bestSellNum:
        answer.append(book)

answer.sort()
print(answer[0])

# 딕셔너리 소팅하는법 아직 찾아봐야 알긴해
# https://codechacha.com/ko/python-sorting-dict/

# sorted는 아예 새로운 리스트 반환, sort는 현재 리스트를 정렬 + sort는 리스트만을 위한 매소드
# https://cigiko.cafe24.com/python-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-sort%EC%99%80-sorted/
