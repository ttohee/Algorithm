num = int(input())

def doOrNot(arr):
    a = len(arr) -1
    do = True
    for i in range(len(arr) // 2):
        if arr[i] == arr.pop():
            do = True
        else:
            do = False
    return do

for i in range(num):
    temp_string = list(input().strip())
    if doOrNot(temp_string):
        print('Do-it')
    else:
        print('Do-it-Not')