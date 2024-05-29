def solution(s):
    answer = ''
    cnt = 1
    for i in s:
        if cnt%2 == 0:
            answer += i.lower()
        else: answer += i.upper()
        if i == ' ': cnt = 0
        cnt += 1
    return answer