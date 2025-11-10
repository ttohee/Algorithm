import sys

while True:
    line = sys.stdin.readline()
    if not line: 
        break
    nums = list(map(int, line.strip().split(' ')))
    print(nums[0] + nums[1])