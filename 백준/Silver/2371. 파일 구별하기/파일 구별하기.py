n = int(input())
arr = []

for _ in range(n):
    string = input().strip().split()[:-1]
    arr.append(' '.join(string)) 

def is_unique(k):
    seen = set()
    for file in arr:
        prefix = ' '.join(file.split()[:k])
        if prefix in seen:
            return False
        seen.add(prefix)
    return True

left, right = 1, max(len(file.split()) for file in arr)
result = right

while left <= right:
    mid = (left + right) // 2
    if is_unique(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)