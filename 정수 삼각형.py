def solution(triangle):
    for i in range(1, len(triangle)):        # 두번째 줄부터 위의 숫자 중 큰 숫자 선택해서 더해주면 된다.
        for j in range(len(triangle[i])):    # 해당 줄 에서 한 원소 씩 보면서 바로 머리 위에 연결된 원소 두개 중 max를 더해줌
            if j==0:                         # 근데 원소가 젤 왼쪽에 있는 머리 양쪽이 아니라 한쪽에만 있으니까 꼼짝없이 걔로 더해줌
                triangle[i][j] += triangle[i-1][0]
            elif j==len(triangle[i])-1:      # 원소가 젤 오른쪽에 있는애면 얘도 더해줄 애 고민할것도 없이 정해짐
                triangle[i][j] += triangle[i-1][-1]
            else:                            # 이제 머리 위에 양쪽 원소 중에 더 큰애로 더해주면
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        
    return max(triangle[-1])                 # 맨 마지막 줄에 위에서부터 큰 수들이 쌓인 sum된 결과가 나오는데 이 중에 최댓값이 정답
