import sys

result = []
words = sys.stdin.read().split()
max_len = max(len(w) for w in words)

for i in range(max_len):
    for j in range(5):
        if i < len(words[j]):
            result.append(words[j][i])

print(''.join(result))