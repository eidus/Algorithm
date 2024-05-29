def solution(number):
    answer = 0
    def combination(arr, n):
        result = []
        if n == 0: return [[]]
        for i in range(len(arr)):
            elem = arr[i]
            for rest in combination(arr[i + 1:], n - 1):
                result.append([elem] + rest)
        return result
    
    aa = combination(number, 3)   
    for i in aa:
        if sum(i) == 0: answer += 1
    return answer