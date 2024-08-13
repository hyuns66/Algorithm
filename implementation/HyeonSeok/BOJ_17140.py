def R(graph):
    for r in range(len(graph)):
        counter = dict()
        temp = list()
        for num in graph[r]:
            if num == 0:
                continue
            if num not in counter.keys():
                counter[num] = 1
            else:
                counter[num] += 1
        sorted_counter = dict(sorted(counter.items(), key = lambda item: (item[1], item[0])))
        for num, count in sorted_counter.items():
            temp.append(num)
            temp.append(count)
        # 100만큼 슬라이싱하고, 나머지를 0으로 채우기
        sliced_temp = temp[:100]
        sliced_temp += [0] * (100 - len(sliced_temp))
        graph[r] = sliced_temp[:]

def C(graph):
    for c in range(len(graph[0])):
        counter = dict()
        temp = list()
        for r in range(len(graph)):
            num = graph[r][c]
            if num == 0:
                continue
            if num not in counter.keys():
                counter[num] = 1
            else:
                counter[num] += 1
        sorted_counter = dict(sorted(counter.items(), key=lambda item: (item[1], item[0])))
        for num, count in sorted_counter.items():
            temp.append(num)
            temp.append(count)
        sliced_temp = temp[:100]
        sliced_temp += [0] * (100 - len(sliced_temp))
        for r in range(len(graph)):
            graph[r][c] = sliced_temp[r]

def count_rc(graph):
    max_r = 0
    max_c = 0
    for r in range(100):
        for c in range(100):
            if graph[r][c] != 0:
                max_c = max(max_c, c)
                max_r = max(max_r, r)
    return max_r, max_c

y, x, k = map(int, input().split())
graph = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    temp = list(map(int, input().split()))
    for j in range(3):
        graph[i][j] = temp[j]

answer = 0
while graph[y-1][x-1] != k:
    if answer > 100:
        answer = -1
        break
    answer += 1
    max_r, max_c = count_rc(graph)
    if max_r >= max_c:
        R(graph)
    else:
        C(graph)
print(answer)