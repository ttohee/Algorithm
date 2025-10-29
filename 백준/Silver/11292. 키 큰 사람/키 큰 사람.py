while(True):
    n = int(input())
    if n == 0 :
        break
        
    student = []
    height = []
    result = []

    for _ in range(n):
        name, h = input().split()
        h = float(h)
        student.append((name, h))
        height.append(h)

    max_h = max(height)

    for name, h in student:
        if h == max_h:
            result.append(name)

    print(' '.join(result))