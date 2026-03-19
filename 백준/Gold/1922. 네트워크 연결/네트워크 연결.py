import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
g = [i for i in range(n+1)]
q = []

for _ in range(m):
    a, b, c = list(map(int, (sys.stdin.readline().split(' '))))
    heapq.heappush(q, (c, a, b))

def find_p(x):
    if g[x] != x:
        g[x] = find_p(g[x])
    return g[x]

def union(a, b):
    a, b = find_p(a), find_p(b)
    if a < b:
        g[b] = a
    else:
        g[a] = b

res = []
while q:
    c, a, b = heapq.heappop(q)
    if find_p(a) != find_p(b):
        res.append(c)
        union(a, b)

print(sum(res))