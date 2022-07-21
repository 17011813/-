두개의 char가 연속되면 pop해서 다 지워지는지

def solution(s):
    stack = list(s)
    q = [stack[0]]
    
    for i in range(1, len(stack)):
        if len(q) == 0 or q[-1] != stack[i]:     # q라는 stack을 만들어놓고, 여기에 저장된 맨 마지막 애랑 stack의 현재 멤버랑 같으면 pop해주고, 다르면 stack에 append 해준다.
            q.append(stack[i])
        else:
            q.pop()

    if len(q)==0: return 1          # 그랬을 때 맨 마지막에 q stack이 텅 비어있으면 다 짝이 있었던거
    return 0
