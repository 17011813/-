def solution(files):
    dic = {}
    for file in files:
        num_start, num_end = 0, 0
        for i in range(1, len(file)):
            if not file[i-1].isdigit() and file[i].isdigit():   # 숫자인지 아닌지 확인
                num_start = i
            if file[i].isdigit() and i == len(file)-1:
                num_end = i
                break
            if file[i-1].isdigit() and not file[i].isdigit():
                num_end = i-1
                break
        head = file[:num_start].lower()
        number = int(file[num_start:num_end+1])
        dic[file] = [head, number]

    dic = sorted(dic.items(), key = lambda x: x[1])  # 딕셔너리에서 value 값 기준으로 정렬

    return [i[0] for i in dic]
