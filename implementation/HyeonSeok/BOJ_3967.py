import sys
from collections import deque

def char2num(char):
    return ord(char)-64

def num2char(num):
    return chr(num+64)

def check(num_graph):
    target = [[0, 2, 5, 7],
            [1, 2, 3, 4],
            [0, 3, 6, 10],
            [7, 8, 9, 10],
            [1, 5, 8, 11],
            [4, 6, 9, 11]]
    for t in target:
        sum = 0
        for idx in t:
            sum += num_graph[idx]
        if sum != 26:
            return False
    return True

def print_graph(num_graph):
    global graph
    empty_graph = [["." for _ in range(9)] for _ in range(5)]
    for y in range(5):
        for x in range(9):
            if graph[y][x] == ".":
                continue
            empty_graph[y][x] = num2char(num_graph.popleft())
    for e in empty_graph:
        print("".join(e))

def dfs(num_graph, dictionary, mask, depth):
    while depth <= 11 and mask[depth]:
        depth += 1
    if depth > 11:
        if check(num_graph):
            print_graph(num_graph)
            exit(0)
    for i in range(1, 13):
        if i in dictionary:
            continue
        num_graph[depth] = i
        dictionary.add(i)
        dfs(num_graph, dictionary, mask, depth+1)
        dictionary.remove(i)
        num_graph[depth] = 0

graph = list()
mask = [False for _ in range(12)]
num_graph = deque([0 for _ in range(12)])
count = 0
dictionary = set()
lines = sys.stdin.readlines()
for line in lines:
    temp = list(line.rstrip())
    for t in temp:
        if t == ".":
            continue
        count += 1
        if t != "x":
            dictionary.add(char2num(t))
            mask[count-1] = True
            num_graph[count-1] = char2num(t)
    graph.append(temp)

# 채워야 할 숫자 (sorted)
nums = list()
for i in range(1, 13):
    if i not in dictionary:
        nums.append(i)
dfs(num_graph, dictionary, mask, 0)