from collections import deque

def check(graph):
    if graph == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        return True
    return False

def move(graph, dif, zero):
    temp = graph[zero+dif]
    graph[zero+dif] = 0
    graph[zero] = temp
    return graph

graph = list()
for i in range(3):
    temp = list(map(int, input().split()))
    graph.extend(temp)
zero = graph.index(0)
q = deque()
visited = set()
visited.add("".join(map(str, graph)))
q.append((graph, zero, 0))
answer = -1
flag = True
while q:
    cur_graph, zero, count = q.popleft()
    if check(cur_graph):
        answer = count
        break
    for dif in [-1, 1, 3, -3]:
        if zero%3 == 0 and dif==-1:
            continue
        if zero%3 == 2 and dif==1:
            continue
        if zero+dif < 0 or zero+dif >= 9:
            continue
        new_graph = move(cur_graph[:], dif, zero)
        pw = "".join(map(str, new_graph))
        if pw not in visited:
            visited.add(pw)
            q.append((new_graph[:], zero+dif, count+1))
print(answer)
