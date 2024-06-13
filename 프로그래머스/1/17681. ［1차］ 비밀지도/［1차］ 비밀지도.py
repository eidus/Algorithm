def make_binary(n, num):
    miro = ['#']*n
    for i in range(n-1, -1, -1):
        if num%2 != 1:
            miro[i]= ' '
        num = num//2
    return miro

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a = make_binary(n, i)
        b = make_binary(n, j)
        print(a, b)
    print(answer)
    
    return answer