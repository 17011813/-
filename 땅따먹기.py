def solution(land):   # 정수 삼각형 문제와 풀이법 동일~~
    for i in range(1, len(land)):  # 두번째 줄부터 바로 위의 행의 숫자 중 큰 숫자 선택해서 더해주면 된다.
        land[i][0] += max(land[i-1][1:])
        land[i][1] += max(land[i-1][0],land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0],land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][:3])

    return max(land[-1])
