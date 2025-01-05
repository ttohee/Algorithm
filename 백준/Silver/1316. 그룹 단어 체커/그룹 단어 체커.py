num = int(input())
count = 0

for _ in range(num):
    check = []
    group = True
    str = input()
    for i in range(len(str)):
        if i > 0 and str[i] != str[i-1]:
            if str[i] in check:
                group = False
                break
        check.append(str[i])
    if group:
        count += 1
print(count)