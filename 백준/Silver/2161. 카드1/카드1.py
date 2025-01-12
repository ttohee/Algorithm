num = int(input())
arr = []
result = []
for i in range(1, num+1):
    arr.append(str(i))
arr.reverse()
while len(arr) > 1:
    result.append(arr.pop())
    card = arr.pop()
    arr.insert(0, card)
result.append(arr[0])
print(' '.join(result))