import sys


def binary_search(array, start, end, tar):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < tar:
            start = mid + 1
        elif array[mid] > tar:
            end = mid
            if start == end:
                break
        else:
            break
    return mid

N = int(sys.stdin.readline())
children = list()
dp = [0] * N
lis = [0] * N
length = 0
for i in range(N):
    children.append(int(sys.stdin.readline()))
for i, child in enumerate(children):
    if length == 0:
        lis[0] = child
        length += 1
    else:
        idx = binary_search(lis, 0, length, child)
        lis[idx] = child
        if idx == length:
            length += 1
print(N - length)
# 3 7 5 2 6 1 4
# 3
# 3 7
# 3 5
# 2 5
# 2 5 6
# 1 5 6
# 1 4 6
