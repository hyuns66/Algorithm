class Node():
    def __init__(self, data, wilde_card, delete_flag):
        self.data = data
        self.wilde_card = wilde_card
        self.delete_flag = delete_flag
        self.children = dict()

class Trie():
    def __init__(self):
        self.head = Node("", True, False)

    def add_file(self, path, deletable):
        cur = self.head
        cur.wilde_card = cur.wilde_card and deletable
        depth = 0
        data = ""
        while depth < len(path):
            char = path[depth]
            data += char
            node = Node(data, deletable, False)
            if char in cur.children.keys():
                node = cur.children[char]
                node.wilde_card = node.wilde_card and deletable
            else:
                cur.children[char] = node
            cur = node
            depth += 1
        cur.delete_flag = deletable

    def remove(self, cur):
        answer = 0
        if cur.wilde_card:
            return 1
        elif cur.delete_flag:
            answer += 1
        for char, node in cur.children.items():
            answer += self.remove(node)
        return answer

t = int(input())
for _ in range(t):
    trie = Trie()
    n1 = int(input())
    for _ in range(n1):
        path = list(input().rstrip())
        trie.add_file(path, True)
    n2 = int(input())
    for _ in range(n2):
        path = list(input().rstrip())
        trie.add_file(path, False)
    print(trie.remove(trie.head))