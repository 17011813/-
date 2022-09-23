def solution(cacheSize, cities):
    if cacheSize == 0: return len(cities) * 5
    answer, cac = 0, []
    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    for i in range(len(cities)):
        if cities[i] in cac:
            cac.remove(cities[i])
            answer += 1
        else:
            if len(cac) >= cacheSize:
                cac.pop(0)
            answer += 5
        cac.append(cities[i])
    return answer
