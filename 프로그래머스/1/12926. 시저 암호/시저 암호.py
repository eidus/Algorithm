def solution(s, n): # 65~ 90, 97~ 122
    answer = ''
    for i in s:
        if i != ' ': 
            if ord(i) <= 90:
                if ord(i)+n > 90: answer += chr(ord(i)+n-26)
                else: answer += chr(ord(i)+n)
            else:
                if ord(i)+n > 122: answer += chr(ord(i)+n-26)
                else: answer += chr(ord(i)+n)
        else: answer += i            
    print(answer)
    return answer