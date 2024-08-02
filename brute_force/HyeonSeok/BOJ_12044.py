def xor(num, count, K, depth):
    if depth >= 4:
        if num[0] ^ num[1] ^ num[2] ^ num[3] == K:
            return count+1
        else:
            return count
    for number in numbers[depth]:
        num.append(number)
        count = xor(num, count, K, depth+1)
        num.pop()
    return count

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list()
    for _ in range(4):
        numbers.append(list(map(int, input().split())))
    answer = 0
    for num in numbers[0]:
        answer = xor([num], answer, K, 1)
    print(f"Case #{tc}: {answer}")