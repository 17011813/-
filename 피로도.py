from itertools import permutations
def solution(k, dungeons):
    maxi = 0
    all_case = list(permutations(dungeons, len(dungeons)))  # 순열로 모든 경우의수 계산
    for case in all_case:
        remain = k
        cnt = 0
        for i in case:
            if i[0] <= remain:
                remain -= i[1]
                cnt += 1
        if cnt > maxi: maxi = cnt       # 가장 많은 던전을 돌 수 있던 경우의 수 출력
    return maxi
