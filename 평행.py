
def solution(dots):
    cnt = 0
    for i in range(4):
        for j in range(i+1, 4):
            if dots[i]==dots[j]:
                cnt+=1
    if cnt == 2: return 1
    if cnt == 1: return 0
    line = []
    for i in range(1,4):
        if dots[0][0] != dots[i][0]:
            line.append((dots[0][1]-dots[i][1]) / (dots[0][0]-dots[i][0]))
    for i in range(2,4):
        if dots[1][0] != dots[i][0]:
            line.append((dots[1][1]-dots[i][1]) / (dots[1][0]-dots[i][0]))
    if dots[2][0] != dots[3][0]:
        line.append((dots[2][1]-dots[3][1]) / (dots[2][0]-dots[3][0]))
    if len(list(set(line))) == len(line): return 0
    return 1
    
    # dots = sorted(dots)  # 우선 x를 기준으로 정렬했을 때
    # print(dots)
    # if dots[1][0] != dots[0][0] and dots[3][0] != dots[2][0]:
    #     a = (dots[1][1]-dots[0][1]) / (dots[1][0]-dots[0][0])
    #     b = (dots[3][1]-dots[2][1]) / (dots[3][0]-dots[2][0])
    #     if a == b: return 1
    # if dots[0] == dots[1] and dots[2] == dots[3]: return 1
    # dots = sorted(dots, key = lambda x: x[1]) # 그 다음 y를 기준으로 정렬했을 때
    # if dots[1][0] != dots[0][0] and dots[3][0] != dots[2][0]:
    #     a = (dots[1][1]-dots[0][1]) / (dots[1][0]-dots[0][0])
    #     b = (dots[3][1]-dots[2][1]) / (dots[3][0]-dots[2][0])
    #     if a == b: return 1 
    # return 0
