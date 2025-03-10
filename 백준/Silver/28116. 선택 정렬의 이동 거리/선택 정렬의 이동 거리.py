def selectionSort(arr, idx, n, res):
    for i in range(n):
        mini = idx[i]

        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp

        temp = idx[arr[mini]-1]
        idx[arr[mini]-1] = idx[arr[i]-1]
        idx[arr[i]-1] = temp

        res[arr[mini]-1] += mini - i
        res[arr[i]-1] += mini - i

n = int(input())
arr = list(map(int, input().split()))

idx = [0 for i in range(n)]
for i in range(n):
    idx[arr[i]-1] = i

res = [0 for i in range(n)]

selectionSort(arr, idx, n, res)
res = list(map(str, res))
print(" ".join(res))