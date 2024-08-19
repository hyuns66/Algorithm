import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

tc = int(input())
for _ in range(tc):
    num = int(input())
    answer = (10**9, 10**9)
    divisors = list()
    divisors = get_divisors(num)
    for a in divisors:
        b = num / a
        if not b.is_integer():
            continue
        middle = (a + int(b)) / 2
        if not middle.is_integer():
            continue
        small = int(middle) - a
        answer = min(answer , (small, int(middle)))
    if answer[0] == 10**9 and answer[1] == 10**9:
        print("IMPOSSIBLE")
    else:
        print(*answer)
