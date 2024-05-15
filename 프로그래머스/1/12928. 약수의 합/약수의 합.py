def solution(n):
    answer = 0
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0: 
            answer += i
            if i is not int(n/i): answer += int(n/i)
    return answer