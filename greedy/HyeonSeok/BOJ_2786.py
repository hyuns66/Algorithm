N = int(input())
h = list()
first_costs = list()
unordered_menu = set()
for i in range(N):
    a, b = map(int, input().split())
    first_costs.append((a, i))
    h.append((b, a-b, i))
    unordered_menu.add(i)

h.sort(reverse=True)
first_costs.sort()

answer = 0
min_diff = 1000000000
max_cost = 0
while h:
    cost, diff, idx = h.pop()
    unordered_menu.remove(idx)
    min_diff = min(min_diff, diff)
    max_cost = max(max_cost, cost)
    answer += cost
    total_cost = answer + min_diff
    for c, i in first_costs:
        if i not in unordered_menu:
            continue
        diff = c - max_cost
        if diff < min_diff:
            total_cost = answer + diff
        break

    print(total_cost)