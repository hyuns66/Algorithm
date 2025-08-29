from collections import deque

def has_key(door, key):
    key_char = door.lower()
    key_idx = ord(key_char) - ord('a')
    if key & (1 << key_idx):
        return True
    else:
        return False
    
def update_key(collected_key, key):
    ck = ord(collected_key) - ord('a')
    return key | (1 << ck)

N, M = map(int, input().split())
graph = list()
for _ in range(N):
    graph.append(list(input().rstrip()))
for y in range(N):
    for x in range(M):
        if graph[y][x] == '0':
            sy = y
            sx = x
            break
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2**6)]
q = deque()
q.append((sy, sx, 0, 0))
answer = -1
while q:
    y, x, count, key = q.popleft()
    if graph[y][x] == '1':
        answer = count
        break
    if graph[y][x] != '.' and graph[y][x] != '0':
        char = graph[y][x]
        if char.islower():
            key = update_key(char, key)
    for dy, dx in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        py = dy + y
        px = dx + x
        if py < 0 or px < 0 or py >= N or px >= M:
            continue
        if visited[key][py][px]:
            continue
        if graph[py][px] == '#':
            continue
        if graph[y][x] != '.' and graph[y][x] != '0':
            if not graph[y][x].islower() and not has_key(graph[y][x], key):
                continue
        visited[key][py][px] = True
        q.append((py, px, count+1, key))
print(answer)