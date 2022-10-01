# heapq가 아니면 통과를 할 수가 없다.

import heapq   # heapq는 일반적인 리스트와 다르게, 가지고 있는 요소를 push, pop 할때마다 자동으로 정렬
def solution(scoville, K):
    answer, sort_scoville = 0, []
    for i in scoville:
        heapq.heappush(sort_scoville, i)         # heappush로 heapq에 넣어주면 작은 원소부터 정렬

    while sort_scoville[0] < K and len(sort_scoville) != 1:  # 제일 작은 원소(맨 앞에 있는 sort_scoville[0])가 K보다 작은 동안만 실행
        heapq.heappush(sort_scoville, heapq.heappop(sort_scoville) + heapq.heappop(sort_scoville) * 2)
        answer += 1      # 맨 앞에 젤 작은 원소 순서대로 하나씩 빼주면서 그 두개 연산한거를 push 해줌
        
    return answer if sort_scoville[0] >= K else -1
