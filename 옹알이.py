def solution(babbling):
    answer = 0
    four = ["aya", "ye", "woo", "ma"]   # 발음할 수 있는 문자들
    check = ["ayaaya", "yeye", "woowoo", "mama"]  # 같은 발음이 연속되므로 발음할 수 없는 예시

    for word in babbling:     # 한 단어씩 보면서
        for checkcheck in check:    # 연속된 단어가 있다면 이 단어는 어차피 발음 못함
            if checkcheck in word:
                word = ""
        if word == "": continue     # 발음 못하는건 그냥 패스
        while(word):                # 문자열에 뭐라도 있는 동안
            is_it = False           # 4개 단어 중에 하나라도 있지 않으면 while문 종료
            for delete_word in four:   # 4개 단어 중에 특정 단어가 문자열에 있다면
                if delete_word in word:
                    word = word.replace(delete_word, "")  # 특정 단어 *모두* 제거
                    is_it = True
            if not is_it: break
            
        if not word:      # 문자열이 4개 단어로만 이루어져 있어서 다 지워져서 문자열이 비어있다면
            answer += 1
    return answer
