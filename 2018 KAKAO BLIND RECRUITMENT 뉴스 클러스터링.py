def solution(str1, str2):
    str1, str2, split_st1, split_st2 = str1.lower(), str2.lower(), [], []
    for i in range(len(list(str1))-1):
        if str1[i].isalpha() and str1[i+1].isalpha(): split_st1.append(str1[i] + str1[i+1])
    for i in range(len(list(str2))-1): 
        if str2[i].isalpha() and str2[i+1].isalpha(): split_st2.append(str2[i] + str2[i+1])    # 두 글자씩 잘라서 split_st1과 split_st2에 넣어줌

    intersection = set(split_st1) & set(split_st2)   # 중복 없는 교집합
    union = set(split_st1) | set(split_st2)          # 중복 없는 합집합
    if not union: return 65536                       # 모두 공집합일 경우에는 65536 리턴

    for i in intersection:    # 중복 없는 교집합의 각 원소마다 두 집합 중 최소로 있는 수를 구해서 계속 더해줌
        i_len += min(split_st1.count(i), split_st2.count(i)) 
    for i in union:           # 중복 없는 합집합의 각 원소마다 두 집합 중 최대로 있는 수를 구해서 계속 더해줌
        u_len += max(split_st1.count(i), split_st2.count(i))
    
    return int(i_len / u_len * 65536)
  
  
  
  이 블로그가 문제 풀다 마지막에 막힐 때 참고하기 좋음
  
  https://jokerldg.github.io/algorithm/2021/05/16/news-cluster.html
