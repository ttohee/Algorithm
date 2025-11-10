t = int(input())

for i in range(0, t):
    nums = list(map(int, input().split()))
    add = nums[0] + nums[1]
    print(f'Case #{i+1}: {add}')