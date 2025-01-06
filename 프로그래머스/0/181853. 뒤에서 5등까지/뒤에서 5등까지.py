def solution(num_list):
    num_list.sort()
    answer = []
    for i in range(5):
        answer.append(num_list[i])
    return answer