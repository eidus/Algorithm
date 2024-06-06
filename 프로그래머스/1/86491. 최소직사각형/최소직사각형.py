def solution(sizes):
    answer = 0
    other_int = 0
    max_int = max(max(sublist) for sublist in sizes)
    max_list = [lst for lst in sizes if max_int in lst]
    if len(max_list) > 1: max_idx = max_list[0].index(max_int) 
    else: max_idx = max_list[0].index(max_int)
    for i in sizes:
        if max_idx == 0:
            if i[0] < i[1] and i[1]<= max_int:
                i[0], i[1] = i[1], i[0]
            if other_int <= i[1]: other_int = i[1]
        elif max_idx == 1:
            if i[0] > i[1] and i[0] <= max_int:
                i[0], i[1] = i[1], i[0]
            if other_int <= i[0]: other_int = i[0]
        print(i)
    print(max_int, other_int)
    answer = max_int * other_int          
    return answer