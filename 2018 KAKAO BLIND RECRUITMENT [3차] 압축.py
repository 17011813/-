def solution(msg):
    answer = []
    initialize = {chr(i+64):i for i in range(1,27)}  # 길이가 1인 모든 단어를 포함하도록 사전을 초기화
    initialize_last_n = 26         # 사전에는 "A":1 이런식으로 저장해서 나중에 value 숫자만 하나씩 올리면서 사전에 업데이트

    while(msg):
        tmp, idx = "", 0
        if msg in initialize: return answer + [initialize[msg]]   # 남은 문자열이 사전에 있으면 최종 출력
        
        for i in range(len(msg)-1):   # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
            tmp += msg[i]
            if tmp + msg[i+1] not in initialize: break       # 다음 문자를 포함했을 때 사전에 없으면 여기 까지 잘라

        answer.append(initialize[tmp])         # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w에 해당하는 사전의 색인 번호를 출력
        initialize_last_n += 1
        initialize[tmp + msg[i+1]] = initialize_last_n # 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록
        
        msg = msg[i+1:]          # msg에서 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 제거
