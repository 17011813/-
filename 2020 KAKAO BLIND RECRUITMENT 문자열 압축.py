def solution(s):
    mini = 100000
    s = list(s)
    for i in range(1, len(s)):
        new_s, point, cnt = [], i, 1
        
        while(point < len(s)):        
            if ''.join(s[point : point + i]) == ''.join(s[point - i : point]):   # 연속으로 같으면 cnt 올려줌
                cnt += 1
            else:
                new_s.append(cnt)       # 다른 문자가 나오면 연속 깨지고 이전의 cnt와 이전의 연속됐던 문자 넣어줌
                new_s.append(''.join(s[point - i : point]))    
                cnt = 1

            point += i
            
        new_s.append(cnt)
        new_s.append(''.join(s[point - i : point]))     # 마지막 문자열도 넣어줌
            
        new_s = list(map(str, new_s))      # 리스트 안에 cnt는 숫자로 들어있어서 '문자'로 변경
        new_s = [i for i in new_s if i not in {'1'}]   # cnt가 1인 경우는 제거

        length = len(''.join(new_s))    # 총 문자열 길이 계산
        
        if length < mini: mini = length
        
    return mini if len(s) != 1 else 1
