from collections import deque
import sys

input = sys.stdin.read
commands = input().splitlines()

count = int(commands[0])
Q = deque()

result = []
for command in commands[1:]:
    if command.startswith("push"):
        _, num = command.split()
        Q.append(num)
    elif command == "pop":
        result.append(Q.popleft() if Q else "-1")
    elif command == "size":
        result.append(str(len(Q)))
    elif command == "empty":
        result.append("1" if not Q else "0")
    elif command == "front":
        result.append(Q[0] if Q else "-1")
    elif command == "back":
        result.append(Q[-1] if Q else "-1")

sys.stdout.write("\n".join(result) + "\n")
