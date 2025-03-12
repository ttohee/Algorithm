from collections import Counter

def solution(arr):
    lengths = []
    for a in arr:
        lengths.append(len(a))
    counter = Counter(lengths)
    return max(counter.values())