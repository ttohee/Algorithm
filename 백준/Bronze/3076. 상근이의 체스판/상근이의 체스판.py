def makeChess(r, c, a, b):
    for i in range(r):
        for _ in range(a):
            row = ""
            for j in range(c):
                color = "X" if (i+j) % 2 == 0 else "."
                row += color * b
            print(row)

r, c = map(int, input().split())
a, b = map(int, input().split())
            
makeChess(r, c, a, b)