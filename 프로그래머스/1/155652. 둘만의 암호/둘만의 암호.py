def solution(s, skip, index):
    answer = ''
    for c in s:
        i = ord(c) # str -> int
        d = index
        while d > 0:
            i += 1
            if i > ord('z'): i = ord('a')
            if chr(i) in skip: d += 1
            d -= 1
        answer += chr(i)
    return answer