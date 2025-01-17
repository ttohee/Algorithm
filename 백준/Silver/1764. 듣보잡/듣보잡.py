import sys

# 입력 처리
N, M = map(int, input().split())
heard = set(sys.stdin.readline().strip() for _ in range(N))  # 듣도 못한 사람
seen = set(sys.stdin.readline().strip() for _ in range(M))  # 보도 못한 사람

# 교집합 구하기
heard_and_seen = sorted(heard & seen)  # 듣도 못한 사람과 보도 못한 사람의 교집합을 사전순으로 정렬

# 출력
print(len(heard_and_seen))  # 듣보잡의 수
for name in heard_and_seen:
    print(name)