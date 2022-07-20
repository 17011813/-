def solution(n):
    answer, num =  "", ["4", "1", "2"]
    while(n>0):
        answer += num[n%3]
        n = n//3 -1 if n%3==0 else n//3
        
    return ''.join(reversed(answer))
