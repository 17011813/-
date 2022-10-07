from collections import deque
def bfs(i, visited, computers, n):
    visited[i] = True      # 지금 방문한 노드는 True로 변경
    save = deque([i])      # 우선 지금 노드 하나 넣어놓고
    while save:            # 큐에 아직 뭐가 있는 동안
        v = save.popleft() # 첫번째 원소 빼내서
        for i in range(n): # 해당 원소랑 연결된 애들 중에 아직 방문되지 않은 노드를 연결시켜준다.
            if computers[v][i] == 1 and not visited[i]:
                visited[i] = True
                save.append(i)           # 그리고 그 연결된 노드랑 연결된 노드들도 검토해야 하니까 큐에 저장해줌
            
def solution(n, computers):
    answer = 0
    visited  = [False] * n          # 우선 다 방문하지 않았다고 설정
    for i in range(n):
        if not visited[i]:          # 모든 노드를 돌면서 방문하지 않았다면
            bfs(i, visited, computers, n)
            answer += 1             # 얘랑 연결된 네트워크 하나가 있는거로 취급
    return answer
