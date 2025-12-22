n = int(input())
num_list = list(map(int, input().split()))
result = []

def isP(n):
    if(n == 1):
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

for numb in num_list:
    if(isP(numb)):
        result.append(numb)

print(len(result))