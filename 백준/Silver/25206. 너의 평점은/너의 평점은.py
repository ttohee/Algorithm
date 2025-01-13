def switch_case(grade):
    if grade == 'A+': return 4.5
    elif grade == 'A0': return 4.0
    elif grade == 'B+': return 3.5
    elif grade == 'B0': return 3.0
    elif grade == 'C+': return 2.5
    elif grade == 'C0': return 2.0
    elif grade == 'D+': return 1.5
    elif grade == 'D0': return 1.0
    elif grade == 'F': return 0.0
    else: return None  

total = 0  
weighted_sum = 0  

for _ in range(20):
    grade_line = input()
    _, num, score = grade_line.split()
    if score == 'P': 
        continue
    num = float(num)
    score = switch_case(score) 
    if score is not None: 
        weighted_sum += num * score  
        total += num 

if total > 0:
    major_rating = weighted_sum / total 
    print(f"{major_rating:.6f}") 
else:
    print("0.000000")
