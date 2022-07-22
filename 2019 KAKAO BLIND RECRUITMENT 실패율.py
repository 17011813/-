import operator                # 이게 dict에서 value로 정렬하는 문법
def solution(N, stages):
    answer = []
    stage = {i+1: 0 for i in range(N)}    # N까지의 Key 값 할당 -- 이런식으로 나옴 {"1":0,"2":0,"3":0,"4":0}

    for i in range(1, N+1):
        not_clear, clear = 0, 0
        for j in range(len(stages)):
            if stages[j] == i: not_clear += 1
            if stages[j] >= i: clear += 1
        if clear > 0: stage[i] = not_clear / clear
        
    stage = sorted(stage.items(), key = operator.itemgetter(1), reverse = True)   # 이게 dict에서 value로 정렬하는 문법
    
    return [i[0] for i in stage]
