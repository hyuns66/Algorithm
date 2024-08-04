N = int(input())
words = list()
max_length = 0
for _ in range(N):
    w = list(input().rstrip())
    max_length = max(max_length, len(w))
    words.append(w)
for i in range(max_length):
    d = dict()
    max_num = 0
    for word in words:
        if len(word) <= i:
            continue
        char = word[i]
        if char not in d.keys():
            d[char] = 1
        else:
            d[char] += 1
        max_num = max(max_num, d[char])
    answer = list()
    for char, num in d.items():
        if num < max_num:
            continue
        answer.append(char)
    answer.sort()
    answer_str = " ".join(answer)
    print(f"{i+1}: {answer_str}")