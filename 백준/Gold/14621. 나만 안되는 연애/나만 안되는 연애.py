import sys

n, m = list(map(int, (sys.stdin.readline().split(' '))))
gender = list((sys.stdin.readline().strip().split(' ')))
edges = []
parent = [i for i in range(n+1)]

for i in range(m):
    u, v, d = list(map(int, (sys.stdin.readline().split(' '))))
    edges.append((d, u, v))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(i, j):
    fi = find(i)
    fj = find(j)
    
    parent[fi] = fj

def kruskal(edgs, n, r):
    edgs.sort()
    edgCount = 0
    valueCount = 0

    for i in range(m):
        if edgCount < n - 1:
            if find(edgs[i][1]) != find(edgs[i][2]) and gender[edgs[i][1] - 1] != gender[edgs[i][2] - 1]:
                union(edgs[i][1], edgs[i][2])
                valueCount += edgs[i][0]
                edgCount += 1

    if edgCount < n - 1:
        return -1
    elif edgCount == n - 1:
        return valueCount
            
print(kruskal(edges, n, m))