def solution(n):
    answer = 0
    if n%(n**(1/2)) == 0: answer = int((n**(1/2)+1)**2)
    else: answer = -1
    return answer