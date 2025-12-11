n = int(input())
l1st = [5000 for _ in range(n+2)]

if n >= 3:
    l1st[3] = 1
if n >= 5:
    l1st[5] = 1

for i in range(6,n+2):
    five_minus = l1st[i-5]
    three_minus = l1st[i-3]
    min_num = five_minus if five_minus < three_minus else three_minus

    if(min_num == 5000): # 포대로 구성할 수 없는 kg
        l1st[i] = 5000
    else:
        l1st[i] = min_num+1

if l1st[n] == 5000:
    print(-1)
else: 
    print(l1st[n])