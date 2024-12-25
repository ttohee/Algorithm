# 테스트 케이스의 개수 입력
count = int(input())
results = []

# 각 테스트 케이스 처리
for _ in range(count):
    a, b = map(int, input().split())
    
    # a의 일의 자리만 고려
    a %= 10
    
    # 일의 자리 패턴이 0이면 결과는 무조건 10 (컴퓨터 번호로 출력)
    if a == 0:
        results.append(10)
        continue

    # 일의 자리별 주기 패턴
    pattern = {
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1],
    }
    
    # 주기의 길이
    cycle = pattern[a]
    cycle_length = len(cycle)
    
    # b-1을 주기의 길이로 나눈 나머지에 해당하는 값이 마지막 데이터 처리 컴퓨터
    index = (b - 1) % cycle_length
    results.append(cycle[index])

# 결과 출력
for result in results:
    print(result)
