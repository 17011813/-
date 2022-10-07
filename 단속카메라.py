def solution(routes):
    answer = 1
    routes.sort(key = lambda x : x[1])  # 정렬 할 때 나가는 시간을 기준으로 정렬해야 논리에 맞아
    spot = routes[0][1]                 # 제일 처음 차량의 마지막 나가는 순간에 찰칵
    
    for i in range(1, len(routes)):     # 두번째 차량부터 돌면서
        if routes[i][0] <= spot:        # 만약 해당 차량이 감시카메라보다 앞에서 달리기 시작했다면 스킵
            continue
        spot = routes[i][1]             # 감시카메라보다 뒤에서 달리기 시작했다면 해당 차량의 맨 마지막 나가는 순간에 감시카메라 달기
        answer += 1                     # 개수 count

    return answer
