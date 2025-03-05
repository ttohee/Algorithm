import sys

startH, startM = map(int, sys.stdin.readline().split())
cookM = int(sys.stdin.readline())

startM += cookM
while startM >= 60:
    startM -= 60
    startH += 1

if startH >= 24:
    startH -= 24

print(startH, startM)