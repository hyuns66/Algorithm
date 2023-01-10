# 단어정렬

import sys
from collections import deque

N = int(sys.stdin.readline())

wordList = []
for i in range(0, N):
    wordList.append(sys.stdin.readline().strip())

wordList = list(set(wordList))  # set을 이용해 중복제거
wordList.sort(key=lambda x: (len(x), x))

for i in range(0, len(wordList)):
    print(wordList[i])

"""
strip()을 쓰면 \n을 없앨 수 있다.

파이썬 정렬, 다중조건으로 한번에 하기
https://dailyheumsi.tistory.com/67
"""
