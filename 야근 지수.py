import heapq
def solution(n, works):
    if sum(works) <= n: return 0    # 만약 works의 모든 수의 합이 n보다 작으면 야근 내에 일 다 처리한거니까 피로도는 무조건 0임
    answer, work = 0, []   # work에 heapq 형식으로 옮겨 담아준다.

    for i in works:
        heapq.heappush(work, -i)   # 원래 heap은 최소힙이기 때문에 제일 큰 수를 pop 하고 싶다면 반대로 최대 힙을 만들어 주면되고, 이는 숫자를 넣어줄 때 -로 넣어주면 된다.

    while(n > 0):
        num = heapq.heappop(work)      # 최대힙 상태이기 때문에 가장 작은수를 추출해오면 사실상 가장 큰 수를 추출해오는 것과 같다.
        heapq.heappush(work, num+1)    # 가장 작은 수(사실 가장 큰 수)에 1을 더해서 큰 수를 하나 줄여준다.
        n -= 1                         # n이 다 소멸 될 때 까지 loop 돌면서 큰 수가 최대한 작아지도록 한다.
    for i in work:
        answer += i**2                 # 남아있는 야근 작업들을 제곱해서 다 더하면 정답
    return answer
