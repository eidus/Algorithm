def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    pp = [0]*4
    for i in range(0, len(answers)):
        if answers[i] == p1[i%5]: pp[1] += 1
        if answers[i] == p2[i%8]: pp[2] += 1
        if answers[i] == p3[i%10]: pp[3] += 1    
        
    m = max(pp)
    for i,v in enumerate(pp):
        if v == m: answer.append(i) 
    print(answer)
    return answer