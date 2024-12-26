n, k = map(int, input().split())
arr = list(range(1, n+1))
r = 0
res = []

while arr:
    r = (r + k - 1) % len(arr)
    res.append(arr.pop(r))

print("<%s>" %(', '.join(map(str,res))))