num = int(input())
for i in range(num):
    print(' ' * ((num - 1) - i), end = '')
    print('*' * (2 * i + 1))
num = num - 1
for i in range(num):
    print(' ' * (i+1), end = '')
    print('*'  * ((num * 2 - 1)-i*2))