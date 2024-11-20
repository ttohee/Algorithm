def solution(arr, intervals):
    inter1 = intervals[0]
    inter2 = intervals[1]
    list1 = arr[inter1[0]:inter1[1]+1]
    list2 = arr[inter2[0]:inter2[1]+1]
    list3 = list1 + list2
    return list3