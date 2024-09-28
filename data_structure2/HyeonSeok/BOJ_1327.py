from collections import deque

def check(arr):
    t = arr[0]
    for num in arr:
        if t > num:
            return False
        t = num
    return True

N, K = map(int, input().split())
array = list(map(int, input().split()))
q = deque()
visited = set()
visited.add("".join(map(str, array)))
q.append((array, 0))
answer = -1
while q:
    arr, count = q.popleft()
    if check(arr):
        answer = count
        break
    for i in range(N-K+1):
        temp = arr[i:i+K]
        temp.reverse()
        new_arr = arr[:i]+temp+arr[i+K:]
        pw = "".join(map(str, new_arr))
        if not pw in visited:
            visited.add(pw)
            q.append((new_arr[:], count+1))
print(answer)