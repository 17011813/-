from collections import deque
def solution(m, n, new_board):
    answer = 0
    board = [[0]*m for i in range(n)]       # 각 원소 'A' 저장하면서 행렬 뒤집을 리스트 생성
    for i in range(m):
        for j in range(n):
            board[j][i] = new_board[i][j]   # 원활한 계산을 위해 행렬 바꿈
    
    while(1):
        end = True        # 한번도 터트려지지 않을 때 까지 무한 반복
        save = []         # save에 터트릴 원소들 저장
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] != 0 and board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                    end = False
                    save.append((i,j))
                    save.append((i+1,j))
                    save.append((i,j+1))
                    save.append((i+1,j+1))   # tuple () 형태로 추가해주면 2차원 리스트도 list(set())으로 중복 제거 가능.
        if end: return answer          # 이번 턴에 한번도 팡 터진게 없다면 터졌던 애들 개수 반환하면서 게임 종료
        save = list(set(save))         # 중복으로 터진 애들 제거
        answer += len(save)            # 이번 턴에 몇개 터졌는지 저장
        for i in save:
            board[i[0]][i[1]] = 0      # 터진 원소들 0으로 값 바꿔줌
        for i in range(n):
            queue = deque(board[i])    # 행마다 보면서 중간에 터진 애들 0인 애들 맨 위로 보내고 남은 살아있는 애들 밑으로 중력그대로 떨어뜨림
            for j in range(m):
                if queue[j] == 0:
                    del queue[j]          # 해당 위치의 0 원소를 삭제하고 맨 위에 0으로 넣어줌
                    queue.appendleft(0)   # 위에다 삽입해야하니까
            board[i] = queue              # board에 업데이트해줌
    
