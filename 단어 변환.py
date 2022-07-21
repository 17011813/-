from collections import deque
def solution(begin, target, words):
    q = deque([begin, 0])
    used = [0]*len(words)   # 각 word마다 일단 아직 사용 안했으니까 0으로 초기화
    while q:
        word, cnt = q.popleft()            # 맨 앞의 값 가져오기
        if word == target:                 # target과 동일하다면 출력
            return cnt 
        for i in range(len(words)):        # words 목록들 중 돌면서
            tmp = 0
            if used[i] == 0:               # 아직 사용 안된 단어라면
                for j in range(len(word)): # q에서 뽑아온 단어의 철자를 하나씩 돌면서
                    if word[j] != words[i][j]:     # 같지 않은 철자가 하나만 있어야 하므로 cnt 해줌
                        tmp += 1
                    if tmp == 1:                  # 서로 1 하나의 철자만 다르다면 후보가 될 수 있으므로 q에 재귀적으로 넣어줌
                        q.append(words[i][j], cnt + 1)
                        used[i] = 1               # 얘는 쓴 애니까 쓴 표시 해줌
    return 0    # 다 돌았는데도 없다면 0 출력
