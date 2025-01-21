from collections import Counter

num = int(input())

for i in range(num):
    letters = list(input().replace(" ", ""))
    counter = Counter(list(letters))
    common = counter.most_common()
    if len(common) > 1 and common[0][1] == common[1][1]:
        print('?')
    else:
        print(common[0][0])