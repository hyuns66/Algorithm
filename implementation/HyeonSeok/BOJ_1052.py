def find_lowest_set_bit(n):
    if n == 0:
        return None, None  # 1이 전혀 없는 경우

    position = 0
    while n & 1 == 0:
        n >>= 1
        position += 1
    
    return position, 1 << position

def count_bit_num(n):
    if n == 0:
        return None, None
    count = 0
    while n:
        count += n&1
        n >>= 1
    return count

N, K = map(int, input().split())
bottles = dict()    # 용량 : 갯수
bottles[1] = N      # 1L 물병 N개
# 가능한 모든 물병 합치기
while True:
    flag = False
    keys = list(bottles.keys())
    for key in keys:
        num = bottles[key]
        if num >= 2:
            flag = True
            new_num = num // 2
            remain = num % 2
            new_key = key << 1
            if new_key not in bottles.keys():
                bottles[new_key] = new_num
            else:
                bottles[new_key] += new_num
            bottles[key] = remain
    if not flag:
        break
bottle_bits = 0
for key, num in bottles.items():
    bottle_bits += key*num

answer = 0
while count_bit_num(bottle_bits) > K:
    position, scale = find_lowest_set_bit(bottle_bits)
    answer += scale
    bottle_bits += scale    
print(answer)