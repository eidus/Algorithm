def solution(price, money, count):
    answer = -1
    take_money = (count * (price + count* price))/2-money
    if take_money > 0 : answer = take_money
    elif take_money <= 0 : answer = 0
    
    return answer