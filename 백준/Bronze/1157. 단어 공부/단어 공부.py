from collections import Counter

words = input().upper()
counter = Counter(words)

max_count = max(counter.values())
most_common = [char for char, count in counter.items() if count == max_count]

if len(most_common) == 1:
    print(most_common[0])
else:
    print('?')