def solution(X, Y):
    X, Y = sorted(list(X)), sorted(list(Y))
    y = ''.join(Y)
    idx, save = 0, [] 
    for x in X:
        if y.find(x, idx) != -1:
            idx = y.find(x, idx) + 1  # 찾은 곳 다음부터 볼꺼니까
            save.append(x)

    if not save: return "-1"   
    if min(save) == '0' and max(save) == '0':   # 0으로만 이루어져 있으면
        return "0"  
    return ''.join(reversed(sorted(save))) 
