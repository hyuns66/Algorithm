# 두 용액

import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

data.sort()

start = 0
end = len(data) -1

answer = []

mix_value = sys.maxsize
while start<end:
    new_mix_value = abs(data[start] + data[end])
    if new_mix_value < mix_value:
        mix_value = new_mix_value
        answer.clear()
        answer.append(data[start])
        answer.append(data[end])

    if data[start] + data[end] < 0:
        start += 1
    else:
        end -= 1

print(*answer)
