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
lis = []
lis_history = []
for idx, num in enumerate(numbers):
    if idx == 0:
        lis.append(num)
        lis_history.append((num, idx))
        continue
    if num <= lis[-1]:
        idx = binary_search(lis, num)
        lis[idx] = num
        lis_history.append((num, idx))
    else:
        lis.append(num)
        lis_history.append((num, len(lis)-1))
lis_length = len(lis)-1
answer_lis = list()
while lis_history:
    num, idx = lis_history.pop()
    if idx == lis_length:
        answer_lis.append(num)
        lis_length -= 1
answer_lis.reverse()
print(len(lis))
print(*answer_lis)
