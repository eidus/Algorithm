def solution(numbers, k):
    answer = 0
    new = (0 + 2*(k-1))%len(numbers)
    answer = numbers[new]
    return answer