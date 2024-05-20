def solution(n):
    answer = '수박'*(n//2) + '수박'*(n%2)
    return answer[0:n]