Q = int(input())
num = 1
add = 0
mul = 1
for _ in range(Q):
    inputs = list(map(int, input().split()))
    a = inputs[0]
    if a == 3:
        answer = mul*num + add
        print(answer)
        continue
    b = inputs[1]
    if a == 2:
        num += b
    elif a == 1:
        add *= b
        mul *= b
    else:
        add += b