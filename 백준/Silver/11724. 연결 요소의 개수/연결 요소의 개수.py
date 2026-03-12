import sys
sys.setrecursionlimit(10000)

n, m = list(map(int, (sys.stdin.readline().split(' '))))
g = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = list(map(int, (sys.stdin.readline().split(' '))))
    g[a][b] = 1
    g[b][a] = 1

def dfs(s):
    visited[s] = 1

    for i in range(n+1):
        if not visited[i] and g[s][i] == 1:
            dfs(i)

count = 0
for j in range(1, n+1):
    if(visited[j] != 1):
        dfs(j)
        count += 1

print(count)