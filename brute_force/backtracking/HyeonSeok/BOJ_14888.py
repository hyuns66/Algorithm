def calculate(orders, numbers):
    num = numbers[0]
    for i in range(len(orders)):
        o = orders[i]
        tar = numbers[i+1]
        if o == "+":
            num += tar
        elif o == "-":
            num -= tar
        elif o == "x":
            num *= tar
        elif o == "/":
            if num < 0:
                num = -num // tar
                num = -num
            else:
                num //= tar
    return num

def backtracking(N, numbers, depth, order_count, orders, answer):
    if depth == N:
        result = calculate(orders, numbers)
        answer[0] = max(answer[0], result)
        answer[1] = min(answer[1], result)
        return
    for idx, o in enumerate(["+", "-", "x", "/"]):
        if order_count[idx] == 0:
            continue
        order_count[idx] -= 1
        orders.append(o)
        backtracking(N, numbers, depth+1, order_count, orders, answer)
        orders.pop()
        order_count[idx] += 1


N = int(input())
numbers = list(map(int, input().split()))
order_count = list(map(int, input().split()))     # sum_n, sub_n, mul_n, mod_n
answer = [-10**10, 10**10]
backtracking(N, numbers, 1, order_count, [], answer)
print(answer[0])
print(answer[1])