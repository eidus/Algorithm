def is_primenum(n):
    for j in range(2,int(n**(1/2))+1):
        if n%j == 0: return False
    return True
def solution(n):
    answer = 0
    for i in range(2, n+1):
        ip = is_primenum(i)
        if ip == True: answer += 1    
    return answer