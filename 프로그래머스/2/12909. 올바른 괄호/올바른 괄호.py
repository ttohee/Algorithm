def solution(s):
    stack = []
    arr = list(s)
    for i in arr:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0