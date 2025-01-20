n, k = map(int, input().split())
arr = []
i = 1

if k == 1:
    print('1')
else:
    while len(arr) < k:
        if n < i:
            break
        if n % i == 0:
            arr.append(i)
        i += 1
    if len(arr) < k:
        print('0')
    else:
        print(arr.pop())