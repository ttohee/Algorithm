import sys

def Queue(arr, command):
    if 'push' in command:
        word, num = command.split(" ")
        arr.append(num)
    elif command == 'pop':
        if len(arr) != 0:
            print(arr.pop(0))
        else:
            print(-1)
    elif command == 'size':
        print(len(arr))
    elif command == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(arr) != 0:
            print(arr[0])
        else:
            print(-1)
    elif command == 'back':
        if len(arr) != 0:
            print(arr[-1])
        else:
            print(-1)

arr = []
count = int(sys.stdin.readline())
commands = sys.stdin.read().split("\n")

for command in commands:
    Queue(arr, command)