# 생태학

import sys

f = open("BOJ_4358_input.txt", 'r')

treeDict = {}
answer = []

lines = f.readlines()
for tree in lines:
    if tree in treeDict.keys():
        treeDict[tree] += 1
    else:
        treeDict[tree] = 1

total = 0
for value in treeDict.values():
    total += value

treeDict = dict(sorted(treeDict.items()))
for tree in treeDict.keys():
    percent = (treeDict[tree] / total) * 100
    answer.append(tree.strip() + " %.4f" % percent)
    # 파이썬 round 반올림의 한계
    # https://docs.python.org/ko/3/library/functions.html?highlight=round#round

for i in answer:
    print(i)

f.close()

