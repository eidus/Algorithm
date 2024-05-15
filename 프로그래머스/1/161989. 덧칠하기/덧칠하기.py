def solution(n, m, section):
    answer = 0
    tmp = 0
    for i in section:
        if i >= tmp:
            tmp = i + m 
            answer += 1
    return answer