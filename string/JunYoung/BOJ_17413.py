# 단어 뒤집기2

import sys

tagStorage = []
wordStorage = []
answer = []

string = sys.stdin.readline().strip() + " "
for i in range(0, len(string)):

    if (string[i] == " ") | (string[i] == "<"):  # 단어 끝
        if string[i] == "<":
            tagStorage.append(string[i])
        for j in range(0, len(wordStorage)):
            answer.append(wordStorage.pop())  # 뒤집어서 저장
        answer.append(string[i])
        continue

    if string[i] == ">":  # 태그 끝
        tagStorage.pop()
        answer.append(string[i])
        continue

    if len(tagStorage) == 0:  # 태그 사이가 아니라면
        wordStorage.append(string[i])  # stack에 넣어놓기
    else:  # 태그 사이라면
        answer.append(string[i])  # 바로 answer에 넣기

result = (''.join(s for s in answer)).strip()
print(result)

"""
리스트를 문자열로
https://codechacha.com/ko/python-convert-list-to-string/
"""
