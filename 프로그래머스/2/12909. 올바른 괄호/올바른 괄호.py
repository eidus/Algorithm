def solution(s):
    answer = True
    tmp = []
    for i in s:
        if i == "(": tmp.append(i)
        if (len(tmp) == 0) and (i == ')'):
            answer = False
            break
        elif(len(tmp) != 0) and (i == ')'):
            tmp.pop()
    if len(tmp) != 0 : answer = False

    return answer