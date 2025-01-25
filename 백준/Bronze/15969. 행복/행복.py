import sys

_ = input()
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
mini = arr[0]
maxi = arr.pop()

print(maxi-mini)