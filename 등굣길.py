def solution(m, n, puddles):
    arr = [[-1]*m for i in range(n)]       # 2차원 배열 초기화                   
    for i in puddles:
        arr[i[1]-1][i[0]-1] = 0            # 웅덩이는 값을 더해주지 않도록 0으로 처리해놈
    for i in range(n):
        for j in range(m):                 # 각 원소마다 돌면서 왼쪽과 위쪽의 값을 더해주면 경우의 수 완성~
            if i == 0 and j == 0: arr[i][j] = 1 # 맨 처음 시작점은 1로 설정
            elif arr[i][j] == 0: continue        # 웅덩이면 스킵
            elif i == 0:
                arr[i][j] = arr[i][j-1]          # 맨 윗 줄은 그 윗줄이 없기 때문에 바로 옆에서만 가져옴
            elif j == 0:
                arr[i][j] = arr[i-1][j]          # 맨 왼쪽 줄은 그 왼족줄이 없기 때문에 바로 위에서만 가져옴
            else:
                arr[i][j] = (arr[i-1][j] + arr[i][j-1])%1000000007   # 계속 최단경로의 개수를 1,000,000,007로 나눈 나머지로 더해주도록 해야 효율성 점수 나옴
    return arr[-1][-1]
