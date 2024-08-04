import sys

def permutation(characters, depth):
    for i in range(len(characters)):
        if depth == 1:
            yield [characters[i]]
        else:
            for next in permutation(characters[:i]+characters[i+1:], depth-1):
                yield [characters[i]] + next


lines = sys.stdin.readlines()
dictionary = set()
scrambled_words = list()
dict_flag = True
for line in lines:
    line = line.rstrip()
    if line == "XXXXXX" and dict_flag:
        dict_flag = False
        continue
    if line == "XXXXXX" and not dict_flag:
        break
    if dict_flag:
        dictionary.add(line)
    else:
        scrambled_words.append(list(line))
for characters in scrambled_words:
    print_dict = set()
    for p in permutation(characters, len(characters)):
        word = "".join(p)
        if word in dictionary:
            print_dict.add(word)
    if print_dict:
        for word in sorted(list(print_dict)):
            print(word)
    else:
        print("NOT A VALID WORD")
    print("******")