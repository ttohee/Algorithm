str = list(input())
a = len(str) - 1
p = True
for i in range(len(str) // 2):
    if(str[i] != str[a]):
        p = False
        break
    a -= 1
if p:
    print('1')
else:
    print('0')