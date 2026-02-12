import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
b = sorted(a)

for _ in range(m):
    d = int(input())
    idx = bisect.bisect_left(b, d)
    
    if idx < n and b[idx] == d:
        print(idx)
    else:
        print(-1)