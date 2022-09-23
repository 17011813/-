def is_right(ss):      # 올바른 괄호 문자열인지 판단
    stack = [ss[0]]
    for i in range(1, len(ss)):
        if ss[i] == '[' or ss[i] == '{' or ss[i] == '(':
            stack.append(ss[i])
        elif ss[i] ==']':
            if stack and stack[-1] == '[':
                stack.pop(-1)
            else:
                stack.append(ss[i])
        elif ss[i] ==')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                stack.append(ss[i])
        elif ss[i] =='}':
            if stack and stack[-1] == '{':
                stack.pop(-1)
            else:
                stack.append(ss[i])
    if stack: return 0   # 올바른 괄호 문자열이 아니면 0 반환

from collections import deque
def solution(s):
    answer = 0
    s = deque(s)               # deque로 바꿔야 rotate 가능
    for i in range(len(s)):
        s.rotate(-1)           # 왼쪽으로 한칸씩 미룸
        if is_right(s) != 0:   # stack에 아무것도 없어서 올바른 문자열이라면
            answer += 1
    return answer
