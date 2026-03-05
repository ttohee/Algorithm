import sys

com_num = int(sys.stdin.readline().rstrip())
connection_num = int(sys.stdin.readline().rstrip())

G = [[0] * com_num for _ in range(com_num)]
for _ in range(connection_num):
    i, j = list(map(int, (sys.stdin.readline().rstrip().split(" "))))
    G[i-1][j-1] = 1
    G[j-1][i-1] = 1

visited = [0] * com_num

def dfs(s):
    visited[s] = 1

    for i in range(com_num):
        if not visited[i] and G[s][i] == 1:
            dfs(i)

dfs(0)

print(sum(visited) - 1)