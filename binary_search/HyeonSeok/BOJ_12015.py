def binary_search(lis, num):
    idx = len(lis) // 2
    start = 0
    end = len(lis)
    while start + 1 != end:
        if lis[idx] >= num:
            end = idx
            idx = (start + end) // 2
        else:
            start = idx
            idx = (start + end) // 2
    if lis[idx] < num:
        return idx+1
    else:
        return idx


N = int(input())
numbers = list(map(int, input().split()))
lis = list()
for idx, num in enumerate(numbers):
    if idx == 0:
        lis.append(num)
        continue
    if num <= lis[-1]:
        idx = binary_search(lis, num)
        lis[idx] = num
    else:
        lis.append(num)
print(len(lis))
        