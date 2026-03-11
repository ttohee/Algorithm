import sys

n, m = list(map(int, (sys.stdin.readline().split(' '))))
graph = []
visited = [[0] * m for _ in range(n)]
q = []
dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]

for _ in range(n):
    line = list(map(int, (list((sys.stdin.readline().strip())))))
    graph.append(line)

def bfs(r, c):
    q.insert(0, (r, c))
    visited[r][c] = 1
    while len(q) > 0:
        row, col = q.pop()
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                graph[nx][ny] = graph[row][col] + 1
                q.insert(0, (nx, ny))
                visited[nx][ny] = 1

bfs(0,0)
print(graph[n-1][m-1])