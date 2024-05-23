def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        try: num = int(s) 
        except ValueError: answer = False
    else: answer = False
    return answer