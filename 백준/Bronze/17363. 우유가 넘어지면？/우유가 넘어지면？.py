import sys

flip = {
    '.' : '.',
    'O' : 'O',
    '-' : '|',
    '|' : '-',
    '/' : '\\',
    "\\" : "/",
    '^' : '<',
    '<' : 'v',
    'v' : '>',
    '>' : '^'
}

n, m = map(int, input().split())
line = sys.stdin.read().split()

result = []
for i in range(m-1, -1, -1):
    rot = []
    for j in range(n):
        rot.append(flip[line[j][i]])
    result.append(rot)

for i in result:
    print(''.join(i))