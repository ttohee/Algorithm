def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for i in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = [(0, 0, 1)] # 시작하는 칸도 1로 치니까 1부터 시작
    visited[0][0] = 1

    while queue:
        x, y, dist = queue.pop(0)

        if x == n - 1 and y == m - 1:
            return dist

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, dist + 1))

    return -1