def is_prime(n):                      # 소수인지 확인하는데 N 수의 제곱근까지만 확인해도 충분히 소수인지 판별 가능
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return 1
    return 0

def solution(n, k):
    jinsu, cnt = "", 0
    while(n > 0):                     # N진수로 바꾸는 공식
        jinsu += str(n%k)       
        n //= k
    split = jinsu[::-1].split('0')    # N진수로 바꾸고 0을 기준으로 분리
    for i in split:
        if i == '1' or i == "": continue
        if is_prime(int(i)) == 0: cnt += 1
    return cnt
