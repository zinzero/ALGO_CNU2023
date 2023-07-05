# 이진 트리의 노드 값을 입력 받아 전위, 중위, 후위 탐색을 하는 프로그램
# 시간 복잡도
# 전위 순회 : O(n)
# 중위 순회 : O(n)
# 후위 순회 : O(n)
# 순회하는 과정에서 모든 노드를 한 번 씩 방문하기 때문에 노드 수의 비례한다.
import time  # 프로그램 실행시간을 알아보기 위한 모듈

start_time = time.time()  # 프로그램 시작 시간


# 이진트리를 만들기 위한 클래스
class TNode:
    def __init__(self, data, left, right):  # 생성자
        self.data = data  # 노드의 데이터
        self.left = left  # 왼쪽 자식을 위한 링크
        self.right = right  # 오른쪽 자식을 위한 링크


# 전위 순회
def preorder(n):
    if n is not None:  # n이 리프 노드가 아닐 경우
        print(n.data, end=" ")  # 현재 노드의 데이터를 출력하고
        if n.left is not None:  # 현재 노드의 left 값이 None이 아닌 경우
            preorder(binary_tree[n.left - 1])  # 현재 노드의 left 노드를 부른다.
        if n.right is not None:  # 현재 노드의 right 값이 None이 아닌 경우
            preorder(binary_tree[n.right - 1])  # 현재 노드의 right 노드를 부른다.


# 중위 순회
def inorder(n):
    if n is not None:  # n이 리프 노드가 아닐 경우
        if n.left is not None:  # 현재 노드의 left 값이 None이 아닌 경우
            inorder(binary_tree[n.left - 1])  # 현재 노드의 left 노드를 부른다.
        print(n.data, end=' ')  # 현재 노드의 데이터를 출력한다.
        if n.right is not None:  # 현재 노드의 right 값이 None이 아닌 경우
            inorder(binary_tree[n.right - 1])  # 현재 노드의 right 노드를 부른다.


# 후위 순회
def postorder(n):
    if n is not None:  # n이 리프 노드가 아닐 경우
        if n.left is not None:  # 현재 노드의 left 값이 None이 아닌 경우
            postorder(binary_tree[n.left - 1])  # 현재 노드의 left 노드를 부른다.
        if n.right is not None:  # 현재 노드의 right 값이 None이 아닌 경우
            postorder(binary_tree[n.right - 1])  # 현재 노드의 right 노드를 부른다.
        print(n.data, end=' ')  # 현재 노드의 데이터를 출력한다.


binary_tree = []  # Tnode 객체를 저장해서 이진트리를 만들기 위한 리스트
n = int(input())  # 노드의 갯수
for _ in range(n):
    data, left, right = map(int, input().split())  # data, left, right 값을 입력 받아 저장

    if left == -1:  # 입력 받은 left가 -1이면
        left = None  # None 값으로 저장

    if right == -1:  # 입력 받은 right가 -1이면
        right = None  # None 값으로 저장

    binary_tree.append(TNode(data, left, right))  # 각각의 값들을 리스트에 저장


root = binary_tree[0]  # 루트 노드

end_time = time.time()  # 프로그램 종료 시간

print("실행시간 : ", end_time - start_time)  # 프로그램 실행시간 출력
# 전위 순회
print('Pre-Order : ', end='')
preorder(root)  # 루트 노드부터 전위 순회 시작
print()

# 중위 순회
print('In-Order : ', end='')
inorder(root)  # 루트 노드부터 중위 순회 시작
print()

# 후위 순회
print('Post-Order : ', end='')
postorder(root)  # 루트 노드부터 후위 순회 시작
print()
