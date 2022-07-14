def solution(id_list, report, k):
    name, wanted, second = {}, [], []
    report = list(set(report))              # 집합set으로 변환 -> list로 변환해서 중복 없앴음~ 
    name = dict.fromkeys(id_list, 0)

    for i in report:
        second.append(i.split()[1])         # second에 신고된 애들 이름 다 적음

    for i in id_list:
        if second.count(i)>=k:              # 신고가 k번 이상 됐으면
            wanted.append(i)
    
    name = dict.fromkeys(id_list, 0)    
    
    for i in report:
        if i.split()[1] in wanted:
            name["{}".format(i.split()[0])] += 1    # 각 유저 당 불량 이용자 신고 횟수 count
        
    return list(name.values())              # 딕셔너리에서 value값들만 출력
