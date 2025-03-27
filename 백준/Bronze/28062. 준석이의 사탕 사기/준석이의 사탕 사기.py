input()
nums = list(map(int, input().split()))
nums.sort()
i = 0

while sum(nums) % 2 != 0:
    if nums[i] % 2 != 0:
        nums.remove(nums[i])
    i += 1

print(sum(nums))