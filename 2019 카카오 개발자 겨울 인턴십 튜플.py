from collections import Counter
def solution(s):
    answer = []
    s = s.replace('{','')   # 우선 문자열에서 필요없는 괄호들 빼고 숫자만 남김
    s = s.replace('}','')
    only_number = s.split(',')       # ','를 기준으로 리스트에 숫자 넣어주기
    
    cnt = Counter(only_number)       # 모든 원소가 각 몇번씩 등장했는지 
    sort = cnt.most_common(100000)   # 내림차순으로 확인 가능
    
    for i in sort:
        answer.append(int(i[0]))     # 내림차순 tuple의 key 값들 순서대로 정답으로 넣어주면됨
    return answer
