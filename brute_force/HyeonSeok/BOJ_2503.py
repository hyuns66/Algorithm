def calc(s, b, number, q100, q10, q1):
    n100 = number // 100
    n10 = (number // 10) % 10
    n1 = number % 10
    strike, ball = 0, 0
    if n100 == n10 or n100 == n1 or n10 == n1 or n100 == 0 or n10 == 0 or n1 == 0:
        return False
    if n100 == q100:
        strike += 1
    if n10 == q10:
        strike += 1
    if n1 == q1:
        strike += 1
    if n100 == q10 or n100 == q1:
        ball += 1
    if n10 == q100 or n10 == q1:
        ball += 1
    if n1 == q100 or n1 == q10:
        ball += 1
    if s == strike and b == ball:
        return True
    else:
        return False

numbers = [True for _ in range(1000)]  # 0 ~ 999 까지 나올 수 있는 숫자 마스킹
N = int(input())
for _ in range(N):
    num, s, b = map(int, input().split())
    n100 = num // 100
    n10 = (num // 10) % 10
    n1 = num % 10
    for number, stat in enumerate(numbers):
        if not stat:
            continue
        numbers[number] = calc(s, b, number, n100, n10, n1)

answer = 0
for stat in numbers:
    if stat:
        answer += 1
print(answer)