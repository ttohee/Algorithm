import sys

num = int(sys.stdin.readline().strip())
parentNum = list(map(int, sys.stdin.readline().split()))
deleteNode = int(sys.stdin.readline().strip())

tree = {i: [] for i in range(num)}
root = -1

for child, parent in enumerate(parentNum):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)

if deleteNode == root:
    print(0)
    sys.exit()

def deleteSub(node):
    if node in tree:
        for child in tree[node]:
            deleteSub(child)
        del tree[node]

deleteSub(deleteNode)

for parent in tree:
    if deleteNode in tree[parent]:
        tree[parent].remove(deleteNode)

leafCount = sum(1 for node in tree if not tree[node])
print(leafCount)