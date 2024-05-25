def solution(n):
    square = []
    answer = 0
    next = n
    num = 0 # 3의 최대 제곱
    
    for i in range(0, int(n**(1/2))):
        if 3**i > n:break
        num = i
        
    for i in range(num, -1, -1):
        square.append(next//(3**i))
        next = n%(3**i)
    for i in range(len(square)):
        answer += square[i] * 3**(i)
    return answer