from collections import Counter
arr = []

count = int(input())
for _ in range(count):
    _, word = input().split('.')
    arr.append(word)
arr.sort()

counter = Counter(arr)
for k, v in counter.items():
    print(k, v)