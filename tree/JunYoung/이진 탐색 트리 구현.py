class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST: # 이진 탐색 트리 클래스
    # 초기에 아무 노드도 없는 상태
    def __init__(self):
        self.root = None

    # 루트 노드부터 시작해서 이진 탐색 트리 규칙에 맞는 위치에 새 노드 삽입
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root
            while True:
                # 삽입하려는 값이 현재 노드보다 작은 경우 왼쪽 자식노드로 이동
                if key<curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(key)
                        break
                else:
                    # 삽입하려는 값이 현재 노드의 값보다 크거나 경우 오른쪽 자식 노드로 이동
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(key)
                        break

    # 이진 탐색 규칙에 따라 특정값이 있는 지 확인(루트노드부터 시작)
    def search(self, key):
        curr = self.root
        # 현재 노드가 존재하고, 찾으려는 값과 현재노드의 값이 같지 않은 경우 반복
        while curr and curr.val !=key:
            # 찾으려는 값이 현재 노드보다 작은 경우 왼쪽 자식 노드로 이동
            if key< curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

##################################################
# lst에 있는 데이터를 활용해서 이진 탐색 트리 생성, search_lst 원소 탐색
def solution(lst, search_lst):
    bst = BST()
    # 리스트의 각 요소를 이용하여 이진 탐색 트리 생성
    for key in lst:
        bst.insert(key)
    result = []
    # 검색 리스트의 각 요소를 이진 탐색 트리에서 검색하고, 검색결과를 리스트에 추가
    for search_val in search_lst:
        if bst.search(search_val):
            result.append(True)
        else:
            result.append(False)
    return result