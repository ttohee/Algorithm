import sys

nodeCount, edgeCount, startNode = map(int, sys.stdin.readline().strip().split(' '))
graph = {i: [] for i in range(1, nodeCount+1)}

for i in range(edgeCount):
    k, v = map(int, sys.stdin.readline().strip().split(' '))
    graph[k].append(v)
    graph[v].append(k)

for k in graph:
    graph[k].sort()

# ------------------------------------------

def dfs(graph, startNode):
 
    res, visited = list(), set()
    
    def _dfs(node):
        if node in visited:
            return

        visited.add(node)
        res.append(node)

        for v in graph[node]:
            _dfs(v)
    _dfs(startNode)
    return res

def bfs(graph, node):
    res = []
    queue = [node]
    visited = set(queue)
    while queue:
        u = queue.pop(0)
        res.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return res

# ------------------------------------------

dfsRes = map(str, dfs(graph, startNode))
bfsRes = map(str, bfs(graph, startNode))

print(" ".join(dfsRes))
print(" ".join(bfsRes))