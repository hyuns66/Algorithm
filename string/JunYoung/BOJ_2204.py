# 도비의 난독증 테스트

import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    wordDict = {}
    for i in range(n):
        word = sys.stdin.readline().strip()
        wordDict[word.lower()] = word

    results = sorted(wordDict.items(), key=lambda x: x[0])
    print(results[0][1])
