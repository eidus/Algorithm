def combination(arr, results, visited, start, n, r):
    if(r == 0): 
        result = [arr[i] for i in range(len(arr)) if visited[i]]
        results.append(sum(result))
        return results

    for i in range(start, n):
        visited[i] = True
        combination(arr,results, visited, i + 1, n, r - 1)
        visited[i] = False
def is_primenum(num):
    for j in range(2, int(num**(1/2))+1):
        if num % j == 0: return False
    return True
        
def solution(nums):
    answer = 0
    results = []
    combination(nums, results, [False]*len(nums), 0, len(nums), 3)
    for i in results:
        tf = is_primenum(i)
        if tf == True: answer += 1
        else: pass    
    return answer