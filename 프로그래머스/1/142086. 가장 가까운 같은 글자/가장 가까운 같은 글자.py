def solution(s):
    answer = [0]*len(s)
    pre = ''
    for i in range(len(s)):
        if s[i] not in pre: 
            answer[i] = -1 
        else:
            index = pre[::-1].find(s[i]) 
            answer[i] += index + 1
        pre += (s[i])
    return answer