import heapq
def solution(operations):
    answer = []
    for i in operations:
        if i.split()[0] == 'I':
            heapq.heappush(answer, int(i.split()[1]))
        elif i == "D -1" and answer:
            heapq.heappop(answer)
        elif i == "D 1" and answer:
            answer.pop()

    if not answer: return [0, 0]
    
    return max(answer), min(answer)
