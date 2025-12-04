s = input()
p = input()
count = 0
start = 0

while start < len(p):
    found = False

    for length in range(len(p) - start, 0, -1):
        cut = p[start: start+length]
        if cut in s:
            start += length
            found = True
            count += 1
            break

    if not found:
        start += 1

print(count)