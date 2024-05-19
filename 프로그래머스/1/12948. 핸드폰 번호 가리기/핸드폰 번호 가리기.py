def solution(phone_number):
    back = phone_number[-4:]
    front = len(phone_number[:-4])*'*'
    answer = front + back
    return answer