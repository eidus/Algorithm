def solution(k, score):
    answer = []
    klist = []
    for i in score:
        klist.append(i)
        klist.sort()
        if len(klist) > k: klist.pop(0)
        answer.append(klist[0])
    return answer