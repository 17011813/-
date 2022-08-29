1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
  
  
def all_right(tmp):       # "올바른 괄호 문자열" 인지 확인
    stack = []
    for i in tmp:
        if i == '(': stack.append('(')      # '('면 스택에 넣어주고
        else:   # if i == ')'
            if len(stack) > 0 : stack.pop()    # 짝이 맞으면 pop
            else: return False      # 안 맞으면 즉시 False 리턴
    return True

def solution(p):
    if len(p) == 0: return ""    # 1번
    l_cnt, r_cnt = 0, 0
    for i in range(len(list(p))):   # 2번
        if p[i] == '(': l_cnt += 1
        else: r_cnt += 1
        if r_cnt == l_cnt: break

    if all_right(p[:i+1]) == True:       # 3번
        return p[:i+1] + solution(p[i+1:])  # 3-1번
    else:   # 4번
        tmp_u = list(p[:i+1][1:-1])    # 4-4번
        for j in range(len(tmp_u)):
            if tmp_u[j] == '(': tmp_u[j] = ')'
            else: tmp_u[j] = '('
        return "(" + solution(p[i+1:]) + ")" + ''.join(tmp_u)   # 4-1번, 4-2번, 4-3번, 4-5번
