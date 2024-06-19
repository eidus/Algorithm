def solution(number, limit, power):
    answer = 0
    c = [0]*number
    for i in range(1, number+1):
        for j in range(1, int(i**(1/2))+1):
            if i%j == 0: 
                c[i-1] += 1
                if j != i/j: c[i-1] += 1
        if c[i-1] > limit: c[i-1] = power
    answer = sum(c)
    return answer