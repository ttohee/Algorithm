import sys
import heapq

n = int(sys.stdin.readline().strip())

min_heap = []

for _ in range(n):
    numbers = list(map(int, sys.stdin.readline().split()))
    for num in numbers:
        if len(min_heap) < n:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappushpop(min_heap, num)# 가장 작은 값 제거 새로운 값 추가

print(min_heap[0])
