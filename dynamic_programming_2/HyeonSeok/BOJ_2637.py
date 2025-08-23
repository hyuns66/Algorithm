def get_base_materials(materials, middle_materials, answer, visited, tar):
    for idx, num in materials[tar]:
        if idx == 0 or num == 0:
            continue
        # 구성부품이 기본부품인 경우 그대로 반영
        if idx not in middle_materials:
            answer[tar][idx] += num
        else:
            # 중간부품인데 dp도 아직 안됐으면 재귀호출하면서 dp 로깅 수행
            if idx not in visited:
                get_base_materials(materials, middle_materials, answer, visited, idx)
            for i, count in enumerate(answer[idx]):
                answer[tar][i] += count * num
    # 이미 dp 로깅 완료됐음 표시
    visited.add(tar)

N = int(input())
M = int(input())
# 각 번호에 해당하는 부품을 만들기 위한 필요 부품 수 저장
materials = [[] for _ in range(N+1)]
# 각 번호에 해당하는 부품을 만들기 위한 기본 부품 수 저장
answer = [[0 for _ in range(N+1)] for _ in range(N+1)]
# 중간부품
middle_materials = set()
for _ in range(M):
    tar, material, num = map(int, input().split())
    materials[tar].append((material, num))
    middle_materials.add(tar)

get_base_materials(materials, middle_materials, answer, set(), N)
for idx, num in enumerate(answer[N]):
    if num == 0:
        continue
    print(idx, num)