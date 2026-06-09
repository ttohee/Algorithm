def solution(answers):
    answer = []
    
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    oneCount = twoCount = threeCount = 0
    oneLoop = twoLoop = threeLoop = 0
    
    for i in range(len(answers)):
        if one[oneLoop] == answers[i]: oneCount += 1
        if two[twoLoop] == answers[i]: twoCount += 1
        if three[threeLoop] == answers[i]: threeCount += 1
        
        oneLoop = (oneLoop + 1) % len(one)
        twoLoop = (twoLoop + 1) % len(two)
        threeLoop = (threeLoop + 1) % len(three)
        
    scores = [oneCount, twoCount, threeCount]
    maxScore = max(scores)
    
    for i in range(len(scores)):
        if scores[i] == maxScore: answer.append(i+1)
        
    return answer