n, m = map(int, input().split())

arr1 = set(input().strip() for _ in range(n))
arr2 = list(input().strip() for _ in range(m))

result = 0
for i in arr2:
    if i in arr1:
        result += 1

print(result)