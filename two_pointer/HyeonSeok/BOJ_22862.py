N, K = map(int, input().split())
S = list(map(int, input().split()))
info = list()
temp = [0, 0]
while S:
    num = S.pop()
    if num & 1 == 1:
        temp[1] += 1
    else:
        if temp[1] == 0:
            temp[0] += 1
        else:
            info.append(temp)
            temp = [1, 0]
info.append(temp)
start = 0
end = 0
count = 0
length = info[start][0]
answer = length
while end < len(info)-1:
    if count+info[end][1] <= K:
        end += 1
        length += info[end][0]
        count += info[end-1][1]
    else:
        length -= info[start][0]
        count -= info[start][1]
        start += 1
    answer = max(answer, length)
print(answer)