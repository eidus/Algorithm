# https://imkh.dev/algorithm-gcd-lcm 참고
def solution(n, m):
    answer = []
    # gcd
    r = 0 
    if n >= m: a, b = n, m
    else:
        a, b = m, n
    while(b != 0):
        r = a % b
        a = b
        b = r
    
    answer.append(a)
    answer.append(n*m/a)
    return answer