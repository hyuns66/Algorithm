import sys

class Node:
    def __init__(self, data, children = None):
        self.data = data
        self.count = 1
        self.children = {} if children == None else children

class Trie:
    def __init__(self):
        self.root = Node("")

    def dfs(self, head : Node, graph, y, x):
        stack = [(y, x, head, graph[y][x], 1)]
        count = 0
        while stack:
            cy, cx, parent, data, depth = stack.pop()
            if depth > 5:
                continue
            char = graph[cy][cx]
            cur_node = Node(data)
            if char not in parent.children.keys():
                count += 1
                parent.children[char] = cur_node
            else:
                cur_node = parent.children[char]
                cur_node.count += 1
            for dy, dx in [[0, 1], [0, -1], [-1, 0], [1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                py = (cy + dy) % len(graph)
                px = (cx + dx) % len(graph[0])
                new_data = data + graph[py][px]
                stack.append((py, px, cur_node, new_data, depth+1))

    def make_trie(self, graph):
        for y in range(len(graph)):
            for x in range(len(graph[0])):
                self.dfs(self.root, graph, y, x)

    def check(self, cur, favorite, depth):
        if cur.data == favorite:
            return cur.count
        char = favorite[depth]
        if char not in cur.children.keys():
            return 0
        return self.check(cur.children[char], favorite, depth+1)

N, M, K = map(int, input().split())
graph = list()
for n in range(N):
    temp = list(input().rstrip())
    graph.append(temp)

favorites = list()
for _ in range(K):
    favorites.append(input().rstrip())

trie = Trie()
trie.make_trie(graph)

for favorite in favorites:
    print(trie.check(trie.root, favorite, 0))
