def change(n, q):
    result = ""
    while n > 0:     # 10진수 -> N진수 바꾸는 공식
        tmp = n % q
        if tmp == 10: tmp = 'A'
        elif tmp == 11: tmp = 'B'
        elif tmp == 12: tmp = 'C'
        elif tmp == 13: tmp = 'D'
        elif tmp == 14: tmp = 'E'
        elif tmp == 15: tmp = 'F'
        result += str(tmp)
        n //= q
    return result[::-1]

def solution(n, t, m, p):
    answer, number = '', "0"
    for i in range(1, 100000):       # 일단 0부터 100000까지 N진수로 변환해서 number에 쭉 이어서 저장해둠
        number += change(i, n)
    for i in range(t):               # 말해야 하는 t번 돌면서 본인 순서의 문자를 출력해줌
        answer += number[p + i*m -1]
    
    return answer
