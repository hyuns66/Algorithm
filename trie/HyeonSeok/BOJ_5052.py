class Node():
    def __init__(self, key, data, flag):
        self.key = key
        self.data = data
        self.flag = flag
        self.children = dict()

class Trie():
    def __init__(self):
        self.head = Node(None, None, False)
    
    def add_number(self, number):
        cur = self.head
        depth = 0
        data = ""
        while depth < len(number):
            char = number[depth]
            data += char
            node = None
            if char in cur.children.keys():
                node = cur.children[char]
                if (depth == len(number) - 1):
                    node.flag = True
            else:
                flag = (depth == len(number)-1)
                node = Node(char, data, flag)
                cur.children[char] = node
            cur = node
            depth += 1
    
    def check(self, cur):
        if cur.flag and len(cur.children) > 0:
            return False
        for key, child in cur.children.items():
            if self.check(child):
                continue
            else:
                return False
        return True


t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    numbers = list()
    for _ in range(n):
        numbers.append(list(input().rstrip()))
    for number in numbers:
        trie.add_number(number)
    if trie.check(trie.head):
        print("YES")
    else:
        print("NO")
    
            