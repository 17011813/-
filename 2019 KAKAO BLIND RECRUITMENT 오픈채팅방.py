def solution(record):
    answer = []
    dic = {}

    for i_rocord in record:
        split_record = i_rocord.split()
        if split_record[0] == 'Enter':
            dic[split_record[1]] = split_record[2]   # id랑 닉네임 입력
            
        elif split_record[0] == 'Change':
            dic[split_record[1]] = split_record[2]   # 이미 enter로 입력된 닉네임 변경
    
    for i in range(len(record)):
        split_record = record[i].split()
        if split_record[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(dic[split_record[1]]))   # 멘트에 맞게 저장된 닉네임 출력
        elif split_record[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(dic[split_record[1]]))
            
    return answer
