def solution(arr):
    answer = []
    answer.append(arr.pop(0))
    for i in arr:
        if answer[-1] == i : continue
        if answer[-1] is not i: answer.append(i)
    return answer