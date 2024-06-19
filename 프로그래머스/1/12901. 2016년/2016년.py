def solution(a, b):
    answer = ''
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    c = 0
    if a > 1:
        for i in range(1,a):
            c += months[i]
    
    answer = days[(c+b-1)%7]
    return answer