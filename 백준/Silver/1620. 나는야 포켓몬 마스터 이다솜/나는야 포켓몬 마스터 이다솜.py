import sys
num, ques = map(int, input().split())

d = {}
re_d = {}

for i in range(1, num+1):
    name = sys.stdin.readline().strip()
    d[str(i)] = name
    re_d[name] = str(i)

for i in range(ques):
    Q = sys.stdin.readline().strip()
    if Q.isdigit():
        print(d[Q])
    else:
        print(re_d[Q])