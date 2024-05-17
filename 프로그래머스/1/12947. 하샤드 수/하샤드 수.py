def solution(x):
    tmp = str(x)
    sc = 0
    for i in tmp:
        sc += int(i)
    if x % sc == 0 : answer = True
    else: answer = False
    return answer