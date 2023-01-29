import copy
import sys
from collections import deque

test_case = list()
while True:
    n, k = map(int, sys.stdin.readline().split())
    if n == k == 0:
        break
    data_set = (k, deque(list(map(int, sys.stdin.readline().split()))))
    test_case.append(data_set)

for data_set in test_case:
    # make tree structure
    tree = dict()
    target_parent = 0
    temp = data_set[1].popleft()
    root = copy.deepcopy(temp)
    q = deque()
    q.append(temp)
    tree[temp] = list()
    parent = 0
    while q and data_set[1]:
        data = data_set[1].popleft()
        if data != temp + 1:
            parent = q.popleft()
        if data == data_set[0]:
            target_parent = parent
        tree[parent].append(data)
        tree[data] = list()
        q.append(data)
        temp = data

    # BFS
    rank = 0
    q = deque()
    q.append(root)
    cnt = 0
    while q:
        node = q.popleft()
        for child in tree[node]:
            q.append(child)
            if child == target_parent:
                for c in tree[node]:
                    if c == target_parent:
                        continue
                    else:
                        cnt += len(tree[c])
    print(cnt)