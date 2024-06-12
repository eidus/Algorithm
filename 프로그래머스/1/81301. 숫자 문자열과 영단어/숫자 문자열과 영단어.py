def solution(s):
    num_list=['zero', 'one', 'two','three','four', 'five','six','seven','eight','nine']
    answer = s
    # print(num_list.index('zero'))
    
    for i in num_list:
        if answer.find(i) != -1:
            answer = answer.replace(i, str(num_list.index(i)))
    print(answer)
    return int(answer)