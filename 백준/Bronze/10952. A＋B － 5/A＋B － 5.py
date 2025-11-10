import sys

while True:
    line = sys.stdin.readline()
    if line.strip() == "0 0": 
        break
    nums = list(map(int, line.strip().split()))
    print(nums[0] + nums[1])