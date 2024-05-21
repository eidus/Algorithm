def solution(s):
    ml = list(s)
    ml.sort(reverse = True)
    answer = ''.join(ml)
    return answer