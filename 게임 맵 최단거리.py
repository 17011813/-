from collections import deque
def solution(maps):
    queue = deque([(0, 0)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우

    while queue:  # bfs 수행
        
        x, y = queue.popleft()           # 해당 원소 빼오면서 제거  -- x,y 이게 현재 캐릭터의 위치다
        for i in range(4):
            xx = x + directions[i][0]    # 얘가 상하좌우로 x랑 y가 어떻게 변하는지 각각 대입해줌 -- xx, yy가 캐릭터가 갈 위치
            yy = y + directions[i][1]
            if 0 <= xx < len(maps[0]) and 0 <= yy < len(maps) and maps[xx][yy] == 1:  # 접근이 가능하고 방문하지 않았던 곳이라면
                maps[xx][yy] = maps[x][y] + 1
                queue.append((xx, yy))
                
    return maps[-1][-1] if maps[-1][-1] > 1 else -1
