count = int(input())
for i in range(count):
    above = 0
    score = list(map(int, input().split()))
    num = score[0]
    del score[0]
    avg = sum(score) / num
    for j in range(num):
        if(score[j] > avg):
            above += 1
    print(f"{above / num * 100:.3f}%")