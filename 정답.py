def solution(logs, events):
    answer = []
    names = []
    name_log = {}
    for i in logs:
        if i.split()[1] not in names:
            names.append(i.split()[1])
    name_log = {i:"" for i in names}
    for i in logs:
        name = i.split()[1]
        name_log[name] += str(i.split()[2]) + " "

    for key, value in name_log.items():
        value_split = value.split()
        for i in range(len(value_split)):
            if value_split[i] != events[i]:
                print(key)
                answer.append(key)
                break

    return sorted(answer) if answer else ["-1"]
