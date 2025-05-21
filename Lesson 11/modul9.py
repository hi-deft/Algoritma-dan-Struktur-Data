class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_path(root, target):
    if root is None:
        return []
    if root.data == target:
        return [root.data]
    left_path = find_path(root.left, target)
    if left_path:
        return [root.data] + left_path
    right_path = find_path(root.right, target)
    if right_path:
        return [root.data] + right_path
    return []

def pre_order(node, result):
    if node:
        result.append(node.data)
        pre_order(node.left, result)
        pre_order(node.right, result)

def in_order(node, result):
    if node:
        in_order(node.left, result)
        result.append(node.data)
        in_order(node.right, result)

def post_order(node, result):
    if node:
        post_order(node.left, result)
        post_order(node.right, result)
        result.append(node.data)

# Membangun pohon
A = Node('Solo')
B = Node('Kartasura')
C = Node('Klaten')
D = Node('Boyolali')
E = Node('Sukoharjo')
F = Node('Delanggu')
G = Node('Prambanan')
H = Node('Wonogiri')
I = Node('Sleman')
J = Node('Yogyakarta')

A.left = B
A.right = C
B.left = D
B.right = E
D.left = H
E.left = I
C.left = F
C.right = G
G.right = J

# Menampilkan hasil
path = find_path(A, 'Yogyakarta')
print("Jalur dari Solo (A) ke Yogyakarta (J):", " -> ".join(path))

pre_result = []
pre_order(A, pre_result)
print("\nPre-order traversal:", ", ".join(pre_result))

in_result = []
in_order(A, in_result)
print("In-order traversal:", ", ".join(in_result))

post_result = []
post_order(A, post_result)
print("Post-order traversal:", ", ".join(post_result))