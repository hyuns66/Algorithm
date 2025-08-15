class Node():
    def __init__(self, data, flag):
        self.data = data
        self.flag = flag
        self.children = dict()

class Trie():
    def __init__(self):
        self.head = Node(None, False)

    def add_word(self, word):
        cur = self.head
        depth = 0
        data = ""
        while depth < len(word):
            char = word[depth]
            data += char
            node = Node(data, False)
            if char in cur.children.keys():
                node = cur.children[char]
            else:
                cur.children[char] = node
            cur = node
            depth += 1
        cur.flag = True

    def search(self, word):
        cur = self.head.children[word[0]]
        depth = 1
        count = 1
        while depth < len(word):
            char = word[depth]
            if len(cur.children) > 1:
                count += 1
            elif cur.flag:
                count += 1
            cur = cur.children[char]
            depth += 1
        return count


while True:
    try:
        s = int(input())
        trie = Trie()
        words = list()
        for _ in range(s):
            word = list(input().rstrip())
            words.append(word)
            trie.add_word(word)
        answer = 0
        for word in words:
            answer += trie.search(word)
        answer /= len(words)
        print(f"{answer:.2f}")
    except EOFError:
        break