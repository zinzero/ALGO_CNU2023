class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(n):
    if n is not None:
        print(n.data, end=" ")
        if n.left is not None:
            preorder(binary_tree[n.left - 1])
        if n.right is not None:
            preorder(binary_tree[n.right - 1])


def inorder(n):
    if n is not None:
        if n.left is not None:
            inorder(binary_tree[n.left - 1])
        print(n.data, end=' ')
        if n.right is not None:
            inorder(binary_tree[n.right - 1])


def postorder(n):
    if n is not None:
        if n.left is not None:
            postorder(binary_tree[n.left - 1])
        if n.right is not None:
            postorder(binary_tree[n.right - 1])
        print(n.data, end=' ')


binary_tree = [TNode(1, 2, 3), TNode(2, 4, 5),
               TNode(3, 6, None), TNode(4, None, None),
               TNode(5, None, None), TNode(6, None, None)]


root = binary_tree[0]

print('Pre-Order : ', end='')
preorder(root)
print()

print('In-Order : ', end='')
inorder(root)
print()

print('Post-Order : ', end='')
postorder(root)
print()
