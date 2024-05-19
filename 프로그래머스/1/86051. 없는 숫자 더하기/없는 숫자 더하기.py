def solution(numbers):
    answer = (9*10)/2
    for i in numbers:
        answer -= i
    return answer