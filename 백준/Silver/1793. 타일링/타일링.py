import sys
input_list = list(map(int, sys.stdin.read().split()))
num_list = [0] * 251
num_list[0] = 1
num_list[1] = 1

def tiling(i):
    a = num_list[i - 1]
    b = num_list[i - 2] * 2
    num_list[i] = a + b

check_poin = 1
for n in input_list:
    if(n > check_poin):
        for i in range(check_poin, n + 1):
            tiling(i)
        check_poin = n
    print(num_list[n])