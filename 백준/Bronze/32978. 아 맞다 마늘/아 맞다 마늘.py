_ = int(input())
arr1 = input().split(' ')
arr2 = input().split(' ')

for i in arr1:
    if i not in arr2:
        print(i)