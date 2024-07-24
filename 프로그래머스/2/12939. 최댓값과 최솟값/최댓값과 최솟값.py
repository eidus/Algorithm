def solution(s):
    answer = ''
    string = ''
    l = []
    for i in s:
        if i == ' ':
            l.append(int(string))
            string = ''
        else:
            string += i
    l.append(int(string))
    answer = f'{min(l)} {max(l)}'
    
    return answer