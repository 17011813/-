import math
def solution(fees, records):
    car_in, answer = {}, {}
    for i in range(len(records)):
        records[i] = records[i].split()    # 문자열 형식의 시각을 분단위로 변환
        records[i][0] = int(records[i][0][:2])*60 + int(records[i][0][3:])
        answer[records[i][1]] = 0          # 각 차 번호당 머무른 시간 담을 딕셔너리 초기화

    for i in range(len(records)):
        if records[i][2] == 'IN':          # 들어온 차는 car_in에 넣어주고
            car_in[records[i][1]] = records[i][0]
        elif records[i][2] == 'OUT':       # 나가는 차는 있었던 시간 계산해서 answer에 넣어줌
            answer[records[i][1]] += records[i][0] - car_in[records[i][1]]
            del car_in[records[i][1]]      # 그리고 나갔기 때문에 car_in 목록에서 제거

    for key, value in car_in.items():      # 목록을 다 돌았는데 여전히 car_in에 남아있는 차들은
        answer[key] += 23*60+59 - value    # 23:59에 출차된 것으로 간주하고 시간 계산
    
    for key, value in answer.items():
        if value <= fees[0]:               # 기본 시간보다 적게 있던 차는 기본 요금 청구
            answer[key] = fees[1]
        else:                              # 기본 시간을 초과한 차는 올림(math.ceil)해서 단위 시간(분) 당 요금 계산
            answer[key] = math.ceil((value - fees[0]) / fees[2]) * fees[3] + fees[1]

    return [value[1] for value in sorted(answer.items())]    # 차량 번호가 작은 자동차부터 오름차순 출력
