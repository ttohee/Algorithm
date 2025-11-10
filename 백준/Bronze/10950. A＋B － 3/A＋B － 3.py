t = int(input())

for i in range(0, t):
    numbers = list(map(int, input().split(' ')))
    print(numbers[0] + numbers[1])