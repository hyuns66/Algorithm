# 세 용액
import sys

N = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))

solution.sort()

min_mix_value = sys.maxsize

answer = []

# 투포인터로 solution

for criterion_idx in range(0, len(solution)):
    start_idx = 0
    end_idx = len(solution) - 1
    while start_idx < end_idx:

        if start_idx == criterion_idx:
            start_idx += 1
            continue
        if end_idx == criterion_idx:
            end_idx -= 1
            continue

        new_mix_value = solution[start_idx] + solution[end_idx] + solution[criterion_idx]
    
        if abs(new_mix_value) < abs(min_mix_value):
            min_mix_value = new_mix_value
            answer.clear()
            answer.append(solution[start_idx])
            answer.append(solution[end_idx])
            answer.append(solution[criterion_idx])

        # 인덱스 갱신
        if new_mix_value < 0:
            start_idx += 1
        else:
            end_idx -= 1

answer.sort()
print(*answer)
